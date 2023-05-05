from flask import Flask, render_template, request, redirect, flash, jsonify, url_for
from werkzeug.utils import secure_filename
import os
import time
import pickle
import calendar
from openvino.runtime import Core

from ir_with_hci import *
from configs.ml_config import *
from configs.flask_config import *


app = Flask(__name__, static_url_path='', static_folder=flask_cfg['static_path'])

def get_ts():
    return str(calendar.timegm(time.gmtime()))

## Load Models and Index
# Load RTMDet-Ins
engine = RTMDetInsEngine()
print("RTMDet-Ins Model Loaded")

# Load Encoder
ie3 = Core()
net3 = ie3.read_model(ir_cfg['encoder_path'])
compiled_model3 = ie3.compile_model(net3, 'CPU')
print("ResNet50Encoder Model Loaded")

# Load Index
with open(ir_cfg['index_path'], "rb") as f:
    ir_index = pickle.load(f)


@app.route("/", methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        # generate ir link to shop
        if request.values['mode'] == "ir":
            ts = request.values['ts']
            selected_id = request.values['selected']
            return url_for('shop', c="irs_{}_{}".format(ts, selected_id))
        
        # response hci
        elif request.values['mode'] == "hci":
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No File Part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No Selected File')
                return redirect(request.url)
            if file:
                ts = get_ts()
                org_path = os.path.join(
                    flask_cfg['cache_cfg']['ir_hci']['prefix'],
                    flask_cfg['cache_cfg']['ir_hci']['org_middle'],
                    "{}_{}".format(ts, file.filename)
                )
                file.save(os.path.join(flask_cfg['static_path'], org_path))
                
                st = time.time()
                output = engine.infer(
                    os.path.join(flask_cfg['static_path'], org_path)
                )
                if output['status'] != 0:
                    return jsonify(output)

                response = build_response(output, ts)
                response['cfg'] = ir_hci_cfg['frontend_cfg']
                response['ts'] = ts

                print("IR HCI response time: {:.4f} seconds".format(time.time()-st))
                return jsonify(response)
        
    return render_template("index.html")

def check_is_ir_search(c):
    if len(c.split("_")) != 3:
        return False
    if c[:3] != "irs":
        return False
    if len(c.split("_")[1]) != 10:
        return False
    return True

@app.route("/shop/<string:c>", methods=['GET', 'POST'])
def shop(c):
    if check_is_ir_search(c):
        ts, selected_id = c.split("_")[1:]

        target_path, target_img = load_from_cache(ts, selected_id, matting=True)
        rank = search_image(compiled_model3, target_img, ir_index)

        response = dict(
            selcted=selected_id,
            target_path="../"+target_path, 
            n_show=ir_cfg['n_show'],
            matched=[])
    
        for i, item in enumerate(rank[:ir_cfg['n_show']]):
            # item[0] -> key
            response['matched'].append((i+1, item[0])) 

        return render_template("shop.html", response=response)
    
    return render_template("shop.html", response=dict(matched=[]))


if __name__ == "__main__":
    app.run()