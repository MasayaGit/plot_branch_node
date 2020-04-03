# coding: UTF-8
import json

def get_branch(layer_json_value):
    #入力層ノードの数はinput_featuresと同じ
    number_of_node = layer_json_value["input_layer"]["input_features"]
    #入力層ノードの次数はinput_layerのout_featuresと同じ
    node_branch = layer_json_value["input_layer"]["out_features"]
    #key次数(横軸) valueノード数(縦軸) 
    return {node_branch:number_of_node}