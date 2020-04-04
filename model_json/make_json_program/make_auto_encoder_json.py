# coding: UTF-8
import json

#モデル構造
#https://github.com/L1aoXingyu/pytorch-beginner/blob/master/08-AutoEncoder/simple_autoencoder.py
def make_json():
    json_value = {
        #encoder
        "layer0":{"input_features":784,"out_features":128,"layer_type":"input"},
        "layer1":{"input_features":128,"out_features":64,"layer_type":"hidden"},
        "layer2":{"input_features":64,"out_features":12,"layer_type":"hidden"},
        "layer3":{"input_features":12,"out_features":3,"layer_type":"hidden"},
        #decoder
        "layer4":{"input_features":3,"out_features":12,"layer_type":"hidden"},
        "layer5":{"input_features":12,"out_features":64,"layer_type":"hidden"},
        "layer6":{"input_features":64,"out_features":128,"layer_type":"hidden"},
        "layer7":{"input_features":128,"out_features":784, "layer_type":"output"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/model_json/json/auto_encoder.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)