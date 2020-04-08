# coding: UTF-8
import json

#モデル構造
#https://github.com/pytorch/examples/blob/master/mnist/main.py
def make_json():
    json_value = {
        "layer0":{"input_channels":1, "out_channels":32,"kernel_size":3,"layer_type":"input","processing_type":"cnn","skip_connection_flag":False},
        "layer1":{"input_channels":32, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection_flag":False},
        "layer2":{"input_features":9216,"out_features":128,"layer_type":"hidden","processing_type":"linear"},
        "layer3":{"input_features":128,"out_features":10, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/simple_cnn.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)