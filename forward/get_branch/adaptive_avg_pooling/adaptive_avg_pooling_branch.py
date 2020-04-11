# coding: UTF-8
import json
import numpy as np

#画像は正方形を仮定
#主にGlobal Average Poolingで使用することを想定
#PyTorch ニューラルネットワーク実装ハンドブック p309を参照
def get_branch(layer_json_value,img_size):
    #ノードの数は画像のピクセル数 (= 縦 * 横 * 入力画像のチャネル数)
    number_of_node = img_size * img_size * layer_json_value["input_channels"]
    #forwardの向きだけを考える場合、次数は１。各ピクセルが一回だけ参照されるようなストライド、プーリングサイズを想定している
    #自分はストライドを指定する
    node_branch = 1
    if layer_json_value["skip_connection"] > 0:
        node_branch += layer_json_value["skip_connection"]
    #np.full(10, 3) なら array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    node_branch_list = np.full(number_of_node, node_branch)
    img_size = layer_json_value["output_size"]
    return node_branch_list,img_size