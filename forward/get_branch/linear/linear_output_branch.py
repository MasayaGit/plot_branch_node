# coding: UTF-8
import json
import numpy as np

#fowardのみを考える場合、linear_output_branchは出力層の一個前の層のノードを考える必要がある。
def get_branch(layer_json_value):
    #出力層の一個前のノードの数はinput_featuresと同じ
    number_of_node = layer_json_value["input_features"]
    #隠れ層ノードの次数はout_featuresと同じ
    node_branch = layer_json_value["out_features"]
    #np.full(10, 3) なら array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    return np.full(number_of_node, node_branch)