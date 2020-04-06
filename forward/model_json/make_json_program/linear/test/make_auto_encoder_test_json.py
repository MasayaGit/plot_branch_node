# coding: UTF-8
import json

#モデル構造
#https://medium.com/@aungkyawmyint_26195/multi-layer-perceptron-mnist-pytorch-463f795b897a
def make_json():
    json_value = {
        #encoder
        "layer0":{"input_features":4,"out_features":2,"layer_type":"input","processing_type":"linear"},
        "layer1":{"input_features":2,"out_features":1,"layer_type":"hidden","processing_type":"linear"},
        #decoder
        "layer2":{"input_features":1,"out_features":2,"layer_type":"hidden","processing_type":"linear"},
        "layer3":{"input_features":2,"out_features":4, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/model_json/json/auto_encoder_test.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)