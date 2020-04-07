# coding: UTF-8
import json

#ImageNetの1000クラス 画像サイズは224×224を想定 ノード数がとても大きい数字になるから
#MaxPool2dを適用した結果の画像のサイズは前の層と変わらないとする
#モデル構造
#http://aidiary.hatenablog.com/entry/20180212/1518404395
def make_json():
    json_value = {
        "layer0":{"input_channels":3, "out_channels":64,"kernel_size":3,"layer_type":"input","processing_type":"cnn"},
        "layer1":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},
        
        #224×224 -> 112*112
        "layer2":{"input_channels":64, "out_channels":64,"stride":2,"layer_type":"hidden","processing_type":"max_pooling"},

        "layer3":{"input_channels":64, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},
        "layer4":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},
        
        #112×112 -> 56*56
        "layer5":{"input_channels":128, "out_channels":128,"stride":2,"layer_type":"hidden","processing_type":"max_pooling"},

        "layer6":{"input_channels":128, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},
        "layer7":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},
        "layer8":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},
        
        #56×56 -> 28*28
        "layer9":{"input_channels":256, "out_channels":256,"stride":2,"layer_type":"hidden","processing_type":"max_pooling"},

        "layer10":{"input_channels":256, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},
        "layer11":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},
        "layer12":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},

        #28×28 -> 14*14
        "layer13":{"input_channels":512, "out_channels":512,"stride":2,"layer_type":"hidden","processing_type":"max_pooling"},

        "layer14":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},
        "layer15":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},
        "layer16":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn"},

        #14×14 -> 7*7
        "layer17":{"input_channels":512, "out_channels":512,"stride":2,"layer_type":"hidden","processing_type":"max_pooling"},

        #classifier 
        #7*7*512 -> 25088
        "layer18":{"input_features":25088,"out_features":4096,"layer_type":"hidden","processing_type":"linear"},
        "layer19":{"input_features":4096,"out_features":4096,"layer_type":"hidden","processing_type":"linear"},
        "layer20":{"input_features":4096,"out_features":1000, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/vgg16.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)