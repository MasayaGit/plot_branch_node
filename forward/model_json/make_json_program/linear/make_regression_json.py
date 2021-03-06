# coding: UTF-8
import json

#モデル構造
#https://docs.microsoft.com/en-us/archive/msdn-magazine/2019/march/test-run-neural-regression-using-pytorch#training-the-model
def make_json():
    json_value = {
        "layer0":{"input_features":13,"out_features":10,"layer_type":"input","processing_type":"linear"},
        "layer1":{"input_features":10,"out_features":10,"layer_type":"hidden","processing_type":"linear"},
        "layer2":{"input_features":10,"out_features":1, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/regression.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)