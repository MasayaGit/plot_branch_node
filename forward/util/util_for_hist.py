# coding: UTF-8
import numpy as np

def get_min_sabun(sort_set_branch):
    min_sabun = None
    for i in range(len(sort_set_branch)):
        if i+1 == len(sort_set_branch):
            break
        current_sabun = sort_set_branch[i+1] - sort_set_branch[i]
        #min_sabunが１0より小さいと、binsがとても多くなるので、continueする
        if current_sabun < 10:
            continue
        if i == 0:
            min_sabun = current_sabun
        if current_sabun < min_sabun:
            min_sabun = current_sabun
    return min_sabun


def get_bin(max_branch,min_sabun):
    bins = 0
    #割り切れないときは+1する。45 / 2 = 22.5。22.5なら２２分割ではなく、23分割にする 
    if max_branch % min_sabun != 0:
        bins = int(max_branch / min_sabun)+1
    else:
        bins = int(max_branch / min_sabun)
    return bins

def get_sort_branch_list(branch_list):
    set_branch_list = set(branch_list)
    sort_set_branch_list = sorted(set_branch_list)
    return sort_set_branch_list

def get_max_set_branch(set_branch_list):
    return max(set_branch_list)

def get_min_set_branch(set_branch_list):
    return min(set_branch_list)
