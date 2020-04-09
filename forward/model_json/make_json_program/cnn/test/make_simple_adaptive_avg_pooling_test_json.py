# coding: UTF-8
import json

#モデル構造
#https://github.com/pytorch/examples/blob/master/mnist/main.py
def make_json():
    json_value = {
        "layer0":{"input_channels":3, "out_channels":5,"kernel_size":3,"layer_type":"input","processing_type":"cnn","skip_connection_flag":False},
        "layer1":{"input_channels":5, "out_channels":7,"kernel_size":2,"layer_type":"hidden","processing_type":"cnn","skip_connection_flag":False},
        
        #画像サイズは output_size * output_sizeになる
        "layer2":{"input_channels":7, "out_channels":7,"output_size":1,"layer_type":"hidden","processing_type":"adaptive_avg_pooling","skip_connection_flag":False},

        #adaptive_avg_poolingによって、input_features = output_size * output_size * input_channels となる
        "layer3":{"input_features":7,"out_features":4,"layer_type":"hidden","processing_type":"linear"},
        "layer4":{"input_features":4,"out_features":2, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/adaptive_avg_pooling_test.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)