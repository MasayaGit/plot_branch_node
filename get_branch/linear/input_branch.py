# coding: UTF-8
import json

def get_branch():
    #json_file = open('./model_json/json/mlp.json', 'r')
    #json_value  = json.load(json_file)

    #入力層ノードの数はinput_featuresと同じ
    number_of_node = json_value["layer1"]["input_layer"]["input_features"]
    #入力層ノードの次数はinput_layerのout_featuresと同じ
    node_branch = json_value["layer1"]["input_layer"]["out_features"]
    #key次数(横軸) valueノード数(縦軸) 
    return {node_branch:number_of_node}