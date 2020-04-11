# coding: UTF-8
import json
import numpy as np

#画像は正方形を仮定
def get_branch(layer_json_value,img_size):
    #ノードの数は画像のピクセル数 (= 縦 * 横 * 入力画像のチャネル数)
    number_of_node = img_size * img_size * layer_json_value["input_channels"]
    #kernel_size * kernel_sizeだけそのピクセルは参照される それがout_channels(=フィルターの数と等価)だけ繰り返される
    node_branch = layer_json_value["kernel_size"] * layer_json_value["kernel_size"] * layer_json_value["out_channels"]
    if layer_json_value["skip_connection"] > 0:
        node_branch += layer_json_value["skip_connection"]
    #np.full(10, 3) なら array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    return np.full(number_of_node, node_branch)