from mmdeploy.apis.utils import build_task_processor
from mmdeploy.utils import get_input_shape, load_config
import torch
from PIL import Image
import numpy as np
import colorsys
from skimage.measure import find_contours
from PIL import Image
import random
import time
import os

from .configs.ml_config import ir_hci_cfg
from .configs.flask_config import flask_cfg


# IR HCI
def random_colors(N, bright=True):
    """
    Generate random colors.
    To get visually distinct colors, generate them in HSV space then
    convert to RGB.
    """
    brightness = 1.0 if bright else 0.7
    hsv = [(i / N, 1, brightness) for i in range(N)]
    colors = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
    random.shuffle(colors)
    return colors


class RTMDetInsEngine:
    def __init__(self) -> None:
        self.cfg = ir_hci_cfg
        self.make_infer_engine()

    def make_infer_engine(self):
        deploy_cfg = self.cfg['rtmdet_ins_cfg']['mmdeploy_cfg_path']
        model_cfg = self.cfg['rtmdet_ins_cfg']['mmdet_cfg_path']
        device = self.cfg['rtmdet_ins_cfg']['device']
        backend_model = [self.cfg['rtmdet_ins_cfg']['onnx_path']]

        # read deploy_cfg and model_cfg
        deploy_cfg, model_cfg = load_config(deploy_cfg, model_cfg)

        # build task and backend model
        self.task_processor = build_task_processor(model_cfg, deploy_cfg, device)
        self.model = self.task_processor.build_backend_model(backend_model)

        # process input image
        self.input_shape = get_input_shape(deploy_cfg)

    def infer(self, img):
        use_rs = False
        if isinstance(img, str):
            image = Image.open(img)
            w, h = image.size
            if max(w, h) > self.cfg['filter_cfg']['rs_threshold']: 
                ratio = self.cfg['filter_cfg']['rs_threshold'] / max(w, h)
                image = image.resize((int(w*ratio), int(h*ratio)))
                use_rs = True
            image = np.array(image)
        elif isinstance(img, np.ndarray):
            image = img
        else:
            # Format Not Support
            return {'status': -1}
        
        if len(image.shape) == 2:
            image = np.repeat(np.expand_dims(image, axis=-1), repeats=3, axis=-1)
        elif len(image.shape) == 3 and image.shape[-1] >= 3:
            image = image[:, :, :3]
        else:
            # Format Not Support
            return {'status': -1}

        model_inputs, _ = self.task_processor.create_input(image, self.input_shape)
        with torch.no_grad():
            result = self.model.test_step(model_inputs)

        output = dict(
            status = 0,
            use_rs = use_rs,
            image = image,
            masks = np.array(result[0].pred_instances.masks).astype('int32'),
            labels = np.array(result[0].pred_instances.labels).astype('int32'),
            bboxes = np.array(result[0].pred_instances.bboxes).astype('int32'),
            scores = np.array(result[0].pred_instances.scores).astype('float32'),
            h = result[0].ori_shape[0],
            w = result[0].ori_shape[1],
        )

        return output
        

def build_response(output, timestamp):
    if output['status'] != 0:
        return output
    
    image = output['image']
    masks = output['masks']
    labels = output['labels']
    bboxes = output['bboxes']
    scores = output['scores']
    h, w = output['h'], output['w']

    colors = random_colors(masks.shape[0])
    centers = []
    res_meta = dict()
    padding = 2
    idx = 0

    if output['use_rs']:
        mid_path = os.path.join(
            flask_cfg['cache_cfg']['ir_hci']['prefix'],
            flask_cfg['cache_cfg']['ir_hci']['rs_middle'],
            "{}_rs.jpg".format(timestamp)
        )
        Image.fromarray(image).save(os.path.join(
            flask_cfg['static_path'],
            mid_path
        ))
    else:
        mid_path = os.path.join(
            flask_cfg['cache_cfg']['ir_hci']['org_middle'],
            "{}_rs.jpg".format(timestamp)
        )

    for i in range(masks.shape[0]):
        
        score_threshold = ir_hci_cfg['filter_cfg']['score_threshold']
        accept_labels = ir_hci_cfg['filter_cfg']['accept_labels']
        overlapping_threshold = ir_hci_cfg['filter_cfg']['overlapping_threshold']
        padding = ir_hci_cfg['mask_cfg']['padding']
        clip_offset = ir_hci_cfg['mask_cfg']['clip_offset']

        if scores[i] < score_threshold or labels[i] not in accept_labels:
            break

        left, top, right, bottom = bboxes[i]
        colorized_mask = np.zeros((h+2*padding, w+2*padding, 4))
        
        # ignore overlapping bboxes
        flag = False
        _c = [(right+left)//2, (bottom+top)//2]
        for c in centers:
            if abs(_c[0] - c[0]) <= overlapping_threshold and abs(_c[1] - c[1]) <= overlapping_threshold:
                flag = True
                break
        if flag:
            continue
        centers.append(_c)
        
        # Colorize Inst Mask
        alpha = 0.3
        color = np.array(list(colors[i]) + [alpha]).reshape((1, 1, 4))
        colorized_mask[padding:padding+h, padding:padding+w, :4] = np.where(
            np.expand_dims(masks[i] == 1, -1),
            color * 255,
            colorized_mask[padding:padding+h, padding:padding+w, :4])

        # Draw Mask Polygon
        contours = find_contours(masks[i], 0.5)[0].astype('int32')
        boundary_color = np.array([255, 255, 255, 255])

        colorized_mask[contours[:, 0], contours[:, 1], :] = boundary_color
        colorized_mask[contours[:, 0], contours[:, 1]+1, :] = boundary_color
        colorized_mask[contours[:, 0], contours[:, 1]-1, :] = boundary_color
        colorized_mask[contours[:, 0]+1, contours[:, 1], :] = boundary_color
        colorized_mask[contours[:, 0]-1, contours[:, 1], :] = boundary_color
        
        # Clip and Save
        my1, my2 = max(0, top-clip_offset),min(h, bottom+clip_offset)
        mx1, mx2 = max(0, left-clip_offset),min(w, right+clip_offset)
        
        m_path = os.path.join(
                flask_cfg['cache_cfg']['ir_hci']['prefix'],
                flask_cfg['cache_cfg']['ir_hci']['m_middle'],
                "{}_m{}.png".format(timestamp, idx)
        )
        im_path = os.path.join(
                flask_cfg['cache_cfg']['ir_hci']['prefix'],
                flask_cfg['cache_cfg']['ir_hci']['im_middle'],
                "{}_im{}.png".format(timestamp, idx)
        )
        res_meta[str(idx)] = dict(
            xmin=int(mx1), xmax=int(mx2), ymin=int(my1), ymax=int(my2),
            m_path=os.path.join("../static", m_path),
            im_path=os.path.join("../static", im_path)
        )

        Image.fromarray(
            colorized_mask[padding:h+padding, padding:w+padding, :][my1:my2, mx1:mx2, :].astype('uint8'), 
            mode='RGBA'
        ).save(os.path.join(flask_cfg['static_path'], m_path))

        Image.fromarray(
            np.concatenate([
                image[my1:my2, mx1:mx2, :].astype('uint8'),
                np.expand_dims(masks[i][my1:my2, mx1:mx2] * 255, axis=-1).astype('uint8')
            ], axis=-1), 
            mode='RGBA'
        ).save(os.path.join(flask_cfg['static_path'], im_path))

        idx += 1

    res_meta['status'] = 0 if len(centers) > 0 else -1
    res_meta['n_targets'] = len(centers)
    res_meta['src_path'] = os.path.join("../static", mid_path)
    res_meta['use_rs'] = int(output['use_rs'])

    return res_meta



# IR Searching
def fill_square(img: np.ndarray, mask: np.ndarray=None, size=256, fill=255, apply_mask=False):
    h, w = img.shape[:2]
    ratio = size/h if h > w else size/w

    img = np.array(Image.fromarray(img.astype('uint8')).resize((int(w*ratio), int(h*ratio))))
    if mask is not None:
        mask = np.array(Image.fromarray(mask.astype('uint8')).resize((int(w*ratio), int(h*ratio))))

    h, w = img.shape[:2]
    img2 = np.ones(shape=(size, size, 3), dtype='int32') * fill
    hst, wst = (size-h)//2, (size-w)//2
    img2[hst:hst+h, wst:wst+w, :] = img
    
    if mask is not None:
        mask2 = np.zeros((size, size), dtype='int32')
        mask2[hst:hst+h, wst:wst+w] = mask

        if apply_mask:
            img2 = img2 * np.expand_dims(mask2, axis=-1) + \
                fill * (1 - (np.expand_dims(mask2, axis=-1)))

        return img2, mask2
    
    return img2

def query_transform(query_img: np.ndarray):
    query_img = fill_square(query_img, size=256, fill=128).astype(np.float32)
    query_img = np.transpose(query_img, [2, 0, 1]) / 255
    img_mean = np.array([0.485, 0.456, 0.406]).reshape((3, 1, 1))
    img_std = np.array([0.229, 0.224, 0.225]).reshape((3, 1, 1))
    query_img -= img_mean
    query_img /= img_std
    return query_img.astype(np.float32).reshape((1, 3, 256, 256))


def rgba2constbg(img: np.ndarray, fill=128):
    _img = img[:, :, :3]
    _mask = img[:, :, 3:4] // 255
    out =  (_img * _mask + np.array([fill]*3) * (1-_mask)).astype('uint8')
    return out

def load_from_cache(timestamp, selected_id, matting=False):
    im_path = os.path.join(
            flask_cfg['cache_cfg']['ir_hci']['prefix'],
            flask_cfg['cache_cfg']['ir_hci']['im_middle'],
            "{}_im{}.png".format(timestamp, selected_id)
    )
    img = np.array(Image.open(os.path.join(flask_cfg['static_path'], im_path)))
    if matting:
        img = rgba2constbg(img)
    else:
        img = img[:, :, :3]
    return im_path, img

def search_image(compiled_model, img_query: np.ndarray, index):
    img_query = query_transform(img_query)
    output = compiled_model.infer_new_request({0: img_query})
    vec = list(output.values())[0]

    res = dict()
    for key, val in index.items():
        sim = 10
        for key2, vec2 in val.items():
            sim = min(sim, 1-np.sum((vec * vec2)))
        res[key] = sim

    rank = sorted(list(res.items()), key=lambda x: x[1])
    return rank