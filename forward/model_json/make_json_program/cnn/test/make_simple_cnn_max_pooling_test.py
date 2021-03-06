# coding: UTF-8
import json

#モデル構造
#https://github.com/pytorch/examples/blob/master/mnist/main.py
def make_json():
    json_value = {
        "layer0":{"input_channels":3, "out_channels":5,"kernel_size":3,"layer_type":"input","processing_type":"cnn","skip_connection":3},
        #各ピクセルが一回だけ参照されるようなストライド、プーリングサイズを想定している。自分はストライドを指定する
        "layer1":{"input_channels":5, "out_channels":5,"stride":2,"layer_type":"hidden","processing_type":"max_pooling","skip_connection":2},
        "layer2":{"input_channels":5, "out_channels":7,"kernel_size":2,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer3":{"input_features":63,"out_features":4,"layer_type":"hidden","processing_type":"linear"},
        "layer4":{"input_features":4,"out_features":2, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/simple_cnn_max_pooling_test.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)