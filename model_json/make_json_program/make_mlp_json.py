# coding: UTF-8
import json

#モデル構造
#https://medium.com/@aungkyawmyint_26195/multi-layer-perceptron-mnist-pytorch-463f795b897a
def make_json():
    json_value = {
        "layer1":{"input_layer":{"input_features":784,"out_features":512}},
        "layer2":{"hidden_layer":{"input_features":512,"out_features":512}},
        "layer3":{"output_layer":{"input_features":512,"out_features":10}}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/model_json/json/mlp.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)