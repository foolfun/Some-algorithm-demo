# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:51:11 2020
@author: zsl
"""
"""
(1)给定正整数 n，确定 n 是否是它的所
有因子之和。比如 n=6 时，它的所有因子分别为 1,2,3，由于
6=1+2+3，所以 6 满足条件.
要求：
输入：正整数 n ；
输出：若 n 是它的所有因子之和，输出 YES ，否则，输出 NO
请给出至少两种方法，并 分析 对比它们的时间复杂度
"""
n = eval(input('输入正整数n:'))
#方法一
print('方法一')
factors = []
for i in range(n-1):
    # print(i+1)
    j = i+1
    if n%j == 0:
        factors.append(j)
    
if sum(factors)==n:
    print('YES')
else:
    print('NO')
    print('时间复杂度是：o(n)')
#方法二
print('方法二')
sums = 0
for i in range(n-1):
    j = i+1
    if n%j == 0:
        sums = sums + j
    if sums > n:
        break
if sums==n:
    print('YES')
else:
    print('NO')
    print('时间复杂度是：o(n)')
"""
(2)编写程序计算斐波那契数列之和：1,2,2,3,5,8,13,21,34
要求：
使用递归方法实现以上算法；
对比递归算法的实现过程，从时间复杂度和空间复杂度上 考虑
是否可以改进递归算法
"""
#递归法
import numpy as np
import time
time_start=time.time()
def F(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return F(n-1)+F(n-2)
def sum_F(n):
    tmp = []
    for i in range(n):
        j=i+1
        tmp.append(F(j))
    return np.array(tmp).sum()

m = eval(input('Input N:'))
print(m,"的斐波那契数列之和:",sum_F(m))
time_end=time.time()
print('递归花费时间',time_end-time_start)
#非递归法
time_start=time.time()
n = int(input("Input N: "))
a = 1
b = 1
sum = 0
for i in range(n):
    sum += a
    a, b = b, a + b
print(n,"的斐波那契数列之和：", sum)
time_end=time.time()
print('非递归花费时间：',time_end-time_start)