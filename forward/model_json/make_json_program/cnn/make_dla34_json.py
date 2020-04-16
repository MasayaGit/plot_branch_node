# coding: UTF-8
import json

#ImageNetの1000クラス 画像サイズは224×224を想定 
#MaxPoolingは除去。
#Blockは単一のCNNのみ
#階層構造になっているCNNを見るだけ。
#モデル構造
#https://arxiv.org/abs/1707.06484
#https://github.com/osmr/imgclsmob/tree/master/pytorch/pytorchcv/models
def make_json():
    json_value = {
        #input
        #stage1
        "layer0":{"input_channels":3, "out_channels":16,"kernel_size":7,"layer_type":"input","processing_type":"cnn","skip_connection":0},
        
        #stage2
        "layer1":{"input_channels":16, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #stage3
        "layer2":{"input_channels":32, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        "layer3":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer4":{"input_channels":128, "out_channels":64,"kernel_size":1,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #stage4
        "layer5":{"input_channels":64, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer6":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer7":{"input_channels":256, "out_channels":128,"kernel_size":1,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        "layer8":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer9":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer10":{"input_channels":448, "out_channels":128,"kernel_size":1,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #stage5
        "layer11":{"input_channels":128, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer12":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer13":{"input_channels":512, "out_channels":256,"kernel_size":1,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        "layer14":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer15":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer16":{"input_channels":896, "out_channels":256,"kernel_size":1,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},        
        
        #stage6
        "layer17":{"input_channels":256, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer18":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer19":{"input_channels":1280, "out_channels":512,"kernel_size":1,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #adaptive_avg_pooling
        #画像サイズは output_size * output_sizeになる
        "layer20":{"input_channels":512, "out_channels":512,"output_size":1,"layer_type":"hidden","processing_type":"adaptive_avg_pooling","skip_connection":0},
        #classifier 
        #input_features : 1*1*512 = 512
        "layer21":{"input_features":512,"out_features":1000, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/dla34.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)