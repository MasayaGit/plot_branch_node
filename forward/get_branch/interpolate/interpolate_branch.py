# coding: UTF-8
import json
import numpy as np

#画像は正方形を仮定
#ESRGANで使用することを想定
def get_branch(layer_json_value,img_size):
    #ノードの数は画像のピクセル数 (= 縦 * 横 * 入力画像のチャネル数)
    number_of_node = img_size * img_size * layer_json_value["input_channels"]
    #1ch1ピクセル対応するノードがscale_factor * scale_factor個のノードに複製されるので
    #次数はscale_factor * scale_factor
    node_branch = layer_json_value["scale_factor"] * layer_json_value["scale_factor"]
    if layer_json_value["skip_connection"] > 0:
        node_branch += layer_json_value["skip_connection"]
    #np.full(10, 3) なら array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    node_branch_list = np.full(number_of_node, node_branch)
    #画像サイズをscale_factor倍する
    img_size = img_size * layer_json_value["scale_factor"]
    return node_branch_list,img_size