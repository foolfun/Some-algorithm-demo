# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:51:45 2020

@author: zsl
"""

'''
（2）给定 n 个元素，这些元素是无序的，分别使用合并排序和快速
排序对 n 个元素进行排序。

要求:写出两种排序算法的完整程序， 测试 两种算法的时间复杂度，对
比它们的优劣
'''

# s start ; e end,快排
def Quick_sort(n, s, e):
    if s >= e:
        return
    x = n[s]
    low = s
    high = e
    while low < high:
        while low < high and x < n[high]:
            high = high - 1
        n[low] = n[high]
        while low < high and x >= n[low]:
            low = low + 1
        n[high] = n[low]
    n[low] = x
    Quick_sort(n, s, low - 1)
    Quick_sort(n, low + 1, e)


# 归并排序
# 对有序的两个序列进行归并
def merge(L1, L2):
    e1 = len(L1) - 1
    e2 = len(L2) - 1
    s1, s2= 0, 0
    L3 = []
    while s1 <= e1 and s2 <= e2:
        if L1[s1] > L2[s2]:
            L3.append(L2[s2])
            s2 = s2 + 1
        else:
            L3.append(L1[s1])
            s1 = s1 + 1
    while s1 > e1 and s2 <= e2:
        L3.append(L2[s2])
        s2 = s2 + 1
    while s1 <= e1 and s2 > e2:
        L3.append(L1[s1])
        s1 = s1 + 1
    return L3


# 拆分，调用归并进行排序
def merge_sort(n):
    if len(n) <= 1:
        return n
    mid = len(n) // 2
    left = merge_sort(n[:mid])
    right = merge_sort(n[mid:])
    return merge(left, right)

import numpy as np
import time
def main2():
    n = np.random.permutation(1000000).tolist()
    print("对含有一百万个数的随机list")
    # n = [5, 3, 4, 2, 1, 6]
    # print(n)
    print('归并排序开始')
    a = time.time()
    merge_sort(n)
    b = time.time()
    # print('归并排序之后的结果：',merge_sort(n))
    print('结束')
    print('快速排序开始')
    c = time.time()
    Quick_sort(n,0,len(n)-1)
    d = time.time()
    # print('快速排序之后的结果：', n)
    print('结束')
    print("merge sort costs %.6f seconds, quick sort costs %.6f seconds" % (b-a,d-c))


main2()