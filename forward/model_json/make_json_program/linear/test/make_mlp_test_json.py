# coding: UTF-8
import json

#テスト用
def make_json():
    json_value = {
        "layer0":{"input_features":4,"out_features":2,"layer_type":"input","processing_type":"linear"},
        "layer1":{"input_features":2,"out_features":3, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/model_json/json/mlp_test.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)