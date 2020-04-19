# coding: UTF-8
import numpy as np

def get_min_sabun(sort_set_branch):
    min_sabun = None
    for i in range(len(sort_set_branch)):
        if i+1 == len(sort_set_branch):
            break
        current_sabun = sort_set_branch[i+1] - sort_set_branch[i]
        if i == 0:
            min_sabun = current_sabun
        if current_sabun < min_sabun:
            min_sabun = current_sabun
    return min_sabun


def get_bin(max_branch,min_sabun):
    bins = 0
    #奇数ときは+1する。45 / 2 = 22.5。22.5なら２２分割ではなく、23分割にする 
    if max_branch % min_sabun == 1:
        bins = int(max_branch / min_sabun)+1
    else:
        bins = int(max_branch / min_sabun)
    return bins