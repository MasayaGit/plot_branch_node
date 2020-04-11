# coding: UTF-8
import json

#モデル構造
#https://github.com/pytorch/examples/blob/master/mnist/main.py
def make_json():
    json_value = {
        "layer0":{"input_channels":3, "out_channels":5,"kernel_size":3,"layer_type":"input","processing_type":"cnn","skip_connection":0},
        "layer1":{"input_channels":5, "out_channels":7,"kernel_size":2,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        "layer2":{"input_features":63,"out_features":4,"layer_type":"hidden","processing_type":"linear"},
        "layer3":{"input_features":4,"out_features":2, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/simple_cnn_test.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)