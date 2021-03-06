# coding: UTF-8
import json

#ImageNetの1000クラス 画像サイズは224×224を想定 
def make_json():
    json_value = {
        #input
        "layer0":{"input_channels":3, "out_channels":64,"kernel_size":7,"layer_type":"input","processing_type":"cnn","skip_connection":0},
        
        #max_pooling ここではストライドと同じカーネルサイズを想定する
        "layer1":{"input_channels":64, "out_channels":64,"stride":2,"layer_type":"hidden","processing_type":"max_pooling","skip_connection":0},

        #skip_connection 64_1
        "layer2":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer3":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        
        #skip_connection 64_2
        "layer4":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer5":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        
        #skip_connection 64_3
        "layer6":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer7":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        
        #skip_connection 128_1
        #次元が異なるskip_connectionだが、単にxを出す側に+1するだけにする。
        "layer8":{"input_channels":64, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer9":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        
        #skip_connection 128_2
        "layer10":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer11":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        
        #skip_connection 128_3
        "layer12":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer13":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        
        #skip_connection 128_4
        "layer14":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer15":{"input_channels":128, "out_channels":128,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        
        #skip_connection 256_1
        #次元が異なるskip_connectionだが、単にxを出す側に+1するだけにする。
        "layer16":{"input_channels":128, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer17":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #skip_connection 256_2
        "layer18":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer19":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #skip_connection 256_3
        "layer20":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer21":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #skip_connection 256_4
        "layer22":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer23":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #skip_connection 256_5
        "layer24":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer25":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #skip_connection 256_6
        "layer26":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer27":{"input_channels":256, "out_channels":256,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #skip_connection 512_1
        #次元が異なるskip_connectionだが、単にxを出す側に+1するだけにする。
        "layer28":{"input_channels":256, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer29":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #skip_connection 512_2
        "layer30":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer31":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #skip_connection 512_3
        "layer32":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer33":{"input_channels":512, "out_channels":512,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},    
        
        #adaptive_avg_pooling
        #画像サイズは output_size * output_sizeになる
        "layer34":{"input_channels":512, "out_channels":512,"output_size":1,"layer_type":"hidden","processing_type":"adaptive_avg_pooling","skip_connection":0},
        
        #classifier 
        #input_features : 1*1*512 = 512
        "layer35":{"input_features":512,"out_features":1000, "layer_type":"output","processing_type":"linear"}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/resnet34.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)