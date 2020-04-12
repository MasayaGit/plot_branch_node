# coding: UTF-8
import json

#モデル構造
#https://github.com/pytorch/examples/blob/master/mnist/main.py
def make_json():
    json_value = {
        "layer0":{"input_channels":3, "out_channels":5,"kernel_size":3,"layer_type":"input","processing_type":"cnn","skip_connection":3},
        #interpolate
        "layer1":{"input_channels":5, "out_channels":5,"scale_factor":2,"layer_type":"hidden","processing_type":"interpolate","skip_connection":0},
        "layer2":{"input_channels":5, "out_channels":7,"kernel_size":2,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        #各ピクセルが一回だけ参照されるようなストライド、プーリングサイズを想定している。自分はストライドを指定する
        "layer3":{"input_channels":7, "out_channels":7,"stride":3,"layer_type":"hidden","processing_type":"max_pooling","skip_connection":0},
        "layer4":{"input_features":112,"out_features":4,"layer_type":"hidden","processing_type":"linear"},
        "layer5":{"input_features":4,"out_features":2, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/simple_interpolate_test.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)