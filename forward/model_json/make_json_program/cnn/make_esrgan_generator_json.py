# coding: UTF-8
import json

#ImageNetの1000クラス 画像サイズは224×224を想定 
#モデル構造
#http://aidiary.hatenablog.com/entry/20180212/1518404395
def make_json():
    json_value = {
        #input
        "layer0":{"input_channels":3, "out_channels":64,"kernel_size":3,"layer_type":"input","processing_type":"cnn","skip_connection":0},
        
        #RRDB start
        #RDB1 start
        #skip_connection":7に注意する +4(RDB1内のskip) +1(RDB1のoutputがでる際に) +1(RRDBのoutputがでる際に) +1(RRDB外)
        "layer1":{"input_channels":64, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":7},
        "layer2":{"input_channels":96, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":3},
        "layer3":{"input_channels":128, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":2},
        "layer4":{"input_channels":160, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer5":{"input_channels":192, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #RDB2 start
        #skip_connection":5に注意する +4(RDB2内のskip) +1(RDB2のoutputがでる際に)
        "layer6":{"input_channels":64, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":5},
        "layer7":{"input_channels":96, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":3},
        "layer8":{"input_channels":128, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":2},
        "layer9":{"input_channels":160, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer10":{"input_channels":192, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        #RDB3 start
        #skip_connection":5に注意する +4(RDB3内のskip) +1(RDB3のoutputがでる際に)
        "layer11":{"input_channels":64, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":5},
        "layer12":{"input_channels":96, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":3},
        "layer13":{"input_channels":128, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":2},
        "layer14":{"input_channels":160, "out_channels":32,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":1},
        "layer15":{"input_channels":192, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        #RRDB end
        
        #RRDBの繰り返しはここでは行わない
        "layer16":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        
        #upsampling
        #interpolate
        "layer17":{"input_channels":64, "out_channels":64,"scale_factor":2,"layer_type":"hidden","processing_type":"interpolate","skip_connection":0},
        "layer18":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        #interpolate
        "layer19":{"input_channels":64, "out_channels":64,"scale_factor":2,"layer_type":"hidden","processing_type":"interpolate","skip_connection":0},
        "layer20":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},

        "layer21":{"input_channels":64, "out_channels":64,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0},
        "layer22":{"input_channels":64, "out_channels":3,"kernel_size":3,"layer_type":"hidden","processing_type":"cnn","skip_connection":0}
    } 
    with open('/Users/info/Desktop/lab/program/plot_branch_node/forward/model_json/json/esrgan_generator.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)