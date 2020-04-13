# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:51:45 2020

@author: zsl
"""

'''
（1）给定 n 个元素，这些元素是有序的（假定为升序），使用二分法
从中查找特定的元素。

要求: 输入 n 个元素，输入某一个特定的值 m ，首先对 n 个元素进行
排序（排序算法任选），输出 m 值的位置序号
'''

import math
# s start ; e end,快排
def Quick_sort(n,s,e):
    if s >= e:
        return
    x = n[s]
    low = s
    high = e
    while low < high:
        while low < high and x < n[high]:
            high = high -1
        n[low]=n[high]
        while low < high and x >= n[low]:
            low = low + 1
        n[high] = n[low]
    n[low] = x
    Quick_sort(n,s,low-1)
    Quick_sort(n,low+1,e)

# 递归二分查找
def BiSearch_pos1(n, low, high, m):
    # 返回 x 在 arr 中的索引，如果不存在返回 -1
    # 基本判断
    if high >= low:
        mid = (high + low) // 2
        # 元素整好的中间位置
        if n[mid] == m:
            return mid
        elif n[mid] > m:
            return BiSearch_pos1(n, low, mid - 1, m) # 元素小于中间位置的元素，只需要再比较左边的元素
        else:
            return BiSearch_pos1(n, mid + 1, high, m) # 元素大于中间位置的元素，只需要再比较右边的元素
    else:
        # 不存在
        return -1

# 非递归的方法的二分查找
def BiSearch_pos2(n,m):
    if m not in n:
        return -1
    low = 0
    high = len(n)-1
    mid = math.ceil((high + low) /2)
    if m == n[mid]:
        return mid
    while True:
        if m < n[mid]:
#            print(n[mid])
            high = mid
            mid = math.ceil((high + low) /2)
            # 因为向上取整，当high为1，low为0的时候会出现死循环，这里做个特殊处理
            if m == n[low]:
                return low
        elif m > n[mid]:
            low = mid
            mid = math.ceil((high + low) /2)
        else:
            return mid

def main1():
    n = [5,3,2,4,1]
    # n = [5,3,2,4,1,6]
    Quick_sort(n,0,len(n)-1)
    print('the list n is ', n)
    # 防止输入其他字符导致的错误
    try:
        m = eval(input('please choose m in the list n (999 is stop):'))
    except Exception:
        m = eval(input('please choose m in the list n (999 is stop):'))
    if m == 999:
        return
    res = BiSearch_pos1(n,0,len(n)-1,m)
    # res = BiSearch_pos2(n,m)
    # 可以循环输入，输入999作为停止标记
    while True:
        if res is not -1:
            print('the position of m is ',res,'\n')
        # 防止输入其他字符导致的错误
        try:
            m = eval(input('please choose m in the list n (999 is stop):'))
        except Exception:
            m = eval(input('please choose m in the list n (999 is stop):'))
        if m == 999:
            return
        res = BiSearch_pos1(n, 0, len(n) - 1, m)
        # res = BiSearch_pos2(n, m)

main1()