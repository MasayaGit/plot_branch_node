# coding: UTF-8
import json

#モデル構造
#https://medium.com/@aungkyawmyint_26195/multi-layer-perceptron-mnist-pytorch-463f795b897a
def make_json():
    json_value = {
        "layer0":{"input_features":784,"out_features":512,"layer_type":"input","processing_type":"linear"},
        "layer1":{"input_features":512,"out_features":512,"layer_type":"hidden","processing_type":"linear"},
        "layer2":{"input_features":512,"out_features":10, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/mlp.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)