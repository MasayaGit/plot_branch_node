# coding: UTF-8
import json

def get_branch(now_layer_json_value,before_layer_json_value):
    #ノードの数はinput_featuresと同じ
    number_of_node = now_layer_json_value["input_features"]
    
    #隠れ層での次数は前と後ろの合計値になる
    front_node_branch = before_layer_json_value["input_features"]
    back_node_branch = now_layer_json_value["out_features"]
    node_branch = front_node_branch + back_node_branch

    #key次数(横軸) valueノード数(縦軸) 
    return {node_branch:number_of_node}