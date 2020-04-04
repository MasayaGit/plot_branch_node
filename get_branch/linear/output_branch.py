# coding: UTF-8
import json

def get_branch(layer_json_value):
    #出力層ノードの数はout_featuresと同じ
    number_of_node = layer_json_value["out_features"]
    #出力層ノードの次数はoutput_layerのinput_featuresと同じ
    node_branch = layer_json_value["input_features"]
    #key次数(横軸) valueノード数(縦軸) 
    return {node_branch:number_of_node}