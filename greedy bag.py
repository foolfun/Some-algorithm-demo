# -*- coding: utf-8 -*-
"""
@author:zsl
"""
'''
（1）根据贪心算法的思想编程实现背包问题：实现假设山洞中有n种宝物，
每种宝物有一定重量w和相应的价值v，毛驴运载能力有限，只能运走m重量的宝物，
一种宝物只能拿一样且宝物可以分割，如何使毛驴运走的宝物价值最大化？
要求：输入量毛驴可承载的最大重量m，若干个宝物重量w和它们的价值v，输出能运走的最大价值。
'''

import numpy as np
import pandas as pd


def bag(m,w,v):
    tmp_n = []
    sum_v = 0
    val = np.array(v)/np.array(w)
    df = pd.DataFrame(data=val,columns=['val'])
    df_new = df.sort_values('val',ascending=False)
    for ind in df_new.index:
        va = df_new.loc[ind,'val']
        # print(va)
        # print(ind)
        if m > 0:
            tmp_w = w[ind]
            if (m - tmp_w) < 0:
                tmp_w = m
            tmp_v = va * tmp_w
            sum_v += tmp_v
            tmp_n.append((ind, tmp_w,tmp_v))
            m = m - w[ind]
        else:
            print('\n贪心算法的输出结果：')
            print('能运走的最大价值：', sum_v)
            print('运走的宝物和其信息如下：')
            for i in tmp_n:
                print('运走的宝物:',i[0],'  选择的重量为:',i[1],'  贡献的价值为:', i[2])
            break
    return


if __name__ == '__main__':
    m = 10  # 毛驴可承载的最大重量，
    w = [2, 3, 4, 7]  # 每个宝物的重量，
    v = [1, 3, 5, 9]  # 每个宝物的价值
    print('输入信息如下：')
    print('毛驴可承载的最大重量:',m)
    print('每个宝物的重量:',w)
    print('每个宝物的价值:',v)
    bag(m,w,v)