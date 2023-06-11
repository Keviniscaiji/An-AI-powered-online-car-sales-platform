# Cars Image Retrieval All-In-One

## 1. Usage

### 1.1 Environment (for Windows 10/11)

- 1. create conda env (optional) (or in a created env)

    ```
    conda create -n projenv python=3.9
    conda activate projenv
    ```

- 2. install torch

    ```
    pip install torch==1.13.1 torchvision==0.14.1
    ```

- 3. install openmmlab dependencies

    ```
    pip install -U openmim
    mim install mmengine
    mim install "mmcv>=2.0.0rc2"
    ```

- 4. install mmdetection and mmdeploy

    ```
    # install VS !!!

    cd <your_work_dir>
    mkdir openmmlab
    cd openmmlab

    git clone -b 1.x https://github.com/open-mmlab/mmdeploy.git
    git clone -b 3.x https://github.com/open-mmlab/mmdetection.git

    cd mmdetection
    pip install -e .

    cd ..
    ```

- 5. install openmmlab onnxruntime support

    ```
    # download mmdeploy-1.0.0rc3-windows-amd64-onnxruntime1.8.1.zip from
    #   - https://github.com/open-mmlab/mmdeploy/releases/download/v1.0.0rc3/mmdeploy-1.0.0rc3-windows-amd64-onnxruntime1.8.1.zip
    pip install .\mmdeploy-1.0.0rc3-windows-amd64-onnxruntime1.8.1\dist\mmdeploy-1.0.0rc3-py3-none-win_amd64.whl
    pip install .\mmdeploy-1.0.0rc3-windows-amd64-onnxruntime1.8.1\sdk\python\mmdeploy_python-1.0.0rc3-cp39-none-win_amd64.whl

    pip install onnxruntime==1.8.1
    ```

- 6. install other dependencies

    ```
    pip install scikit-image matplotlib pillow opencv-python openvino
    ```

### 1.2 Environment (for Ubuntu)

- 1. same as above

- 2. install torch

    ```
    pip install torch==1.13.1 torchvision==0.14.1 --index-url https://download.pytorch.org/whl/cpu
    ```

- 3~4. same as above

- 5. install openmmlab onnxruntime support

    ```
    # install MMDeploy
    wget https://github.com/open-mmlab/mmdeploy/releases/download/v1.0.0rc3/mmdeploy-1.0.0rc3-linux-x86_64-onnxruntime1.8.1.tar.gz
    tar -zxvf mmdeploy-1.0.0rc3-linux-x86_64-onnxruntime1.8.1.tar.gz
    cd mmdeploy-1.0.0rc3-linux-x86_64-onnxruntime1.8.1
    pip install dist/mmdeploy-1.0.0rc3-py3-none-linux_x86_64.whl
    pip install sdk/python/mmdeploy_python-1.0.0rc3-cp39-none-linux_x86_64.whl
    cd ..

    # install inference engine: ONNX Runtime
    pip install onnxruntime==1.8.1
    wget https://github.com/microsoft/onnxruntime/releases/download/v1.8.1/onnxruntime-linux-x64-1.8.1.tgz
    tar -zxvf onnxruntime-linux-x64-1.8.1.tgz

    # add follows to ~/.bashrc
    export ONNXRUNTIME_DIR=$(pwd)/onnxruntime-linux-x64-1.8.1
    export LD_LIBRARY_PATH=$ONNXRUNTIME_DIR/lib:$LD_LIBRARY_PATH

    source ~/.bashrc
    ```

- 6. install other dependencies

    ```
    pip install scikit-image matplotlib pillow opencv-python
    ```

### 1.3 Convert IR Encoder pdparam to ONNX Model 

- `in PaddlePaddle env with GPU`
- `for other team member, please skip this step`

```
python d2s.py
paddle2onnx --model_dir ./ckpts/static --model_filename encoder_d20_ckpt_100.pdmodel --params_filename encoder_d20_ckpt_100.pdiparams --save_file ./ckpts/encoder_d20_ckpt_100.onnx
```

### 1.4 Convert RTMDet-Ins pth to ONNX Model

- `in openmmlab env with GPU`
- `for other team member, please skip this step`

Under mmdeploy folder

```
python tools/deploy.py configs/mmdet/instance-seg/instance-seg_rtmdet-ins_onnxruntime_static-640x640.py <mmdetection_dir>/configs/rtmdet/rtmdet-ins_tiny_8xb32-300e_coco.py <checkpoints_dir>/rtmdet-ins_tiny_8xb32-300e_coco_20221130_151727-ec670f7e.pth --work-dir <work_dir> --device cpu
```

### 1.5 Trouble Shooting (Windows 10/11)

```
# 1.
# onnxruntime.capi.onnxruntime_pybind11_state.Fail: class `End2EndModel` in mmdeploy/codebase/mmdet/deploy/object_detection_model.py: [ONNXRuntimeError] : 1 : FAIL : Failed to load library, error code: 193

copy onnxruntime.dll in <PATH>/onnxruntime-win-x64-1.8.1/lib to <YOUR_ENV_PATH>/Lib/site-packages/mmdeploy/lib
```