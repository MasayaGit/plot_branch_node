# coding: UTF-8
import json

def renew_dic(all_branch_node_dict,get_branch_node_dict):
    intersection_keys = all_branch_node_dict.keys() & get_branch_node_dict.keys()
    for key in intersection_keys:
        get_branch_node_dict[key] = all_branch_node_dict[key] + get_branch_node_dict[key]
    all_branch_node_dict.update(get_branch_node_dict)
    return None
    