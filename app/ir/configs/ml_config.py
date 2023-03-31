import os

proj_path = "/home/student/FYP/FYP/app/ir"

ir_hci_cfg = dict(
    rtmdet_ins_cfg=dict(
        mmdeploy_cfg_path='/home/student/workspace/openmmlab/mmdeploy/configs/mmdet/instance-seg/instance'
                          '-seg_rtmdet'
                          '-ins_onnxruntime_static-640x640.py',
        mmdet_cfg_path='/home/student/workspace/openmmlab/mmdetection/configs/rtmdet/rtmdet'
                       '-ins_tiny_8xb32-300e_coco.py',
        onnx_path=os.path.join(proj_path, "ckpts/end2end.onnx"),
        device='cpu',
        max_bboxes=100
    ),
    filter_cfg=dict(
        score_threshold=0.3,
        accept_labels=[2, 7],
        overlapping_threshold=5,
        n_max=20,
        rank_mode='score',  # accept: area/center/score
        rs_threshold=1000
    ),
    mask_cfg=dict(
        alpha=0.3,
        padding=2,
        clip_offset=5
    ),
    frontend_cfg=dict(
        canvas_size=500,  # px
        enable_anime=1,  # True: 1, False: 0
        enable_rs=1,  # True: 1, False: 0
        anime_length=8,
        anime_speed=0.5,
        anime_rs_ratio=1.2,
        padding=10,  # px
    )
)

ir_cfg = dict(
    database_path="./database",
    index_path=os.path.join(proj_path, "index/index.pkl"),
    encoder_path=os.path.join(proj_path, "ckpts/encoder_d20_ckpt_400.onnx"),
    ndata=20,
    ntest=20,
    e=300,
    n_show=10
)
