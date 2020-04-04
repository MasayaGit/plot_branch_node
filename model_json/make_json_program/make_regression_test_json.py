# coding: UTF-8
import json

#モデル構造
def make_json():
    json_value = {
        "layer0":{"input_features":4,"out_features":2,"layer_type":"input"},
        "layer1":{"input_features":2,"out_features":3,"layer_type":"hidden"},
        "layer2":{"input_features":3,"out_features":1, "layer_type":"output"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/model_json/json/regression_test.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)