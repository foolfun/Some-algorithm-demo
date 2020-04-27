# -*- coding: utf-8 -*-

"""
@author: zsl
"""


'''
（1）给定 n 个矩阵{A 0 ,A 1 ,A 2 , …, A n-1 }，其中 Ai，i=0, …, n-1 的维数为
p i *p i+1 ，并且A i 和A i+1 是可乘的。考察这n个矩阵的连乘积A 0 A 1 A 2 …A n-1 ，
由于矩阵乘法满足结合律，所以计算矩阵的连乘可以有多种不同的计算次序。
结合动态规划思想，编程确定 n 个矩阵的连乘次序，使得按照这个次数计算矩阵连乘，需要的“数乘”次数最少。
要求：
输入:矩阵个数 n ，以及每一个矩阵的尺寸；30,35,15,5,10,20
输出:最佳矩阵连乘次序和数乘次数。
'''
import numpy as np

def MatrixChain(P, n):
    m = np.zeros([n,n],dtype=int)  # 初始化备忘录
    s = np.zeros([n,n],dtype=int)  # 初始化标记函数
    for r in range(2,n+1):
        for i in range(n-r+1):  # 左边界i
           j = i+r-1
           m[i,j]=m[i+1,j]+P[i]*P[i+1]*P[j+1]
           s[i,j] = i
           for k in range(i,j):
                t = m[i,k]+m[k+1,j]+P[i]*P[k+1]*P[j+1]
                if t < m[i,j]:
                    m[i,j]=t
                    s[i,j]=k
    return m,s

def Track_MatrixChain(s,low,high):
    if high == low:
        return 'A%d' % low
    else:
        tmp = s[low,high]
        res = ''
        res += '('+Track_MatrixChain(s,low,tmp)
        res += Track_MatrixChain(s, tmp + 1, high) + ')'
        return res


def main():
   n = eval(input("请输入矩阵个数："))
   P = list(eval(input("请输入矩阵的尺寸，可以连续输入【输入示例：30，35，15；代表A1,A2的尺寸分别为30*35，35*15】：")))
   m1,s1 = MatrixChain(P,n)
   res = Track_MatrixChain(s1,0,n-1)
   print("最佳矩阵连乘次序:",res[1:-1])
   print("最佳数乘次数:",m1[0,4])
   print("\n算法过程中：")
   print('备忘录矩阵：\n',m1)
   print('标记矩阵：\n',s1)

main()