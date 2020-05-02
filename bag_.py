# -*- coding: utf-8 -*-
"""
...
"""
'''
（2）有 n 个物品和购物车的容量，每个物品的重量为 w[i]，价值为
v[i]，购物车的容量为 W，选若干个物品放入购物车，使它们的总价
值最大。结合动态规划思想，编程实现以上 0/1 背包问题
'''


def bag(n, y, w, v):
    """
    测试数据：
    n = 4  物品的数量，
    y = 10 能承受的重量，
    w = [2,3,4,7] 每个物品的重量，
    v = [1,3,5,9] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(y + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, y + 1):
            value[i][j] = value[i - 1][j]
            # 购物车总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    for x in value:
        print(x)
    return value


def TrackSolution(n, y, w, value):
    print('最大价值为:', value[n][y])
    x = [False for i in range(n)]
    j = y
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('购物车中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i+1, '个,', end='')


if __name__ == '__main__':
    n = 4  # 物品的数量，
    y = 10  # 购物车能承受的重量，
    w = [2, 3, 4, 7]  # 每个物品的重量，
    v = [1, 3, 5, 9]   # 每个物品的价值
    value = bag(n, y, w, v)
    TrackSolution(n, y, w, value)