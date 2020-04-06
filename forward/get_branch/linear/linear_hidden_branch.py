# coding: UTF-8
import json
import numpy as np

def get_branch(layer_json_value,):
    #隠れ層ノードの数はinput_featuresと同じ
    number_of_node = layer_json_value["input_features"]
    #隠れ層ノードの次数はout_featuresと同じ
    node_branch = layer_json_value["out_features"]
    ##np.full(10, 3) なら array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    return np.full(number_of_node, node_branch)