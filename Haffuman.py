# -*- coding: utf-8 -*-
"""
@author:zsl
"""
'''
（2）编程实现哈夫曼编码过程。
要求：输入若干字符和对应的权重，
输出对该字符序列的哈夫曼编码结果使用01序列编码
'''
import pandas as pd
# 节点类
class Node:
    def __init__(self,frequency=0,name=None):
        self.name = name
        self.left = None
        self.right = None
        self.father = None
        self.frequency = frequency

    def is_left(self):
        return self.father.left == self

# 创建Huffman树
def Haffuman_tree(node_sequence):
    # 这样的copy方式不会影响原来的node_sequence的内容，但是原来里面的node，因为下列操作的，而有father等值的改变
    sequence = node_sequence[:]
    while len(sequence) > 1:
        sequence.sort(key=lambda item: item.frequency)  # 重新排序，递增
        left = sequence.pop(0)  # 取出最小的两个作为左右节点
        right = sequence.pop(0)
        new_node = left.frequency + right.frequency
        # 构造新节点，作为左右节点的父节点
        node_father = Node(new_node)
        node_father.left = left
        node_father.right = right
        # 给左右节点添加父节点
        left.father = node_father
        right.father = node_father
        sequence.append(node_father)  # 加到后面
    sequence[0].father = None  # root没有父节点
    return sequence[0]  # 返回root，根据root能依次寻找到各个节点


# Huffman编码
def Huffman_encoding(nodes, root):
    node_names = [] #存储节点名字
    huffman_code = [''] * len(nodes)  # len(nodes)：需要返回的哈夫曼编码的节点数
    for i in range(len(nodes)):
        node = nodes[i]
        node_names.append(node.name)
        while node != root:  # 一直回溯到root为止
            if node.is_left():
                huffman_code[i] = '0' + huffman_code[i]  # 为父节点的左节点，将对应节点的哈夫曼编码加0，因为是倒推，所以加在前面
            else:
                huffman_code[i] = '1' + huffman_code[i]  # 为父节点的左节点，将对应节点的哈夫曼编码加1
            node = node.father  # 回溯
    B = 0
    print('编码如下：')
    for j in range(len(node_names)):
        print(node_names[j],'---',huffman_code[j])
        B += len(huffman_code[j])*df.loc[node_names[j],'w']
    print('平均传输位数为：',B/100)
    return


if __name__ == '__main__':
    s = ['a', 'b', 'c', 'd', 'e', 'f']
    w = [45, 13, 12, 16, 9, 5]
    print('输入如下')
    for i in range(len(s)):
        print(s[i],'的权值:',w[i])
  # 先用df排序
    df = pd.DataFrame(data=w, columns=['w'],index=s)
    df = df.sort_values('w')
    node_sequence = []
    for ind in df.index:
        node = Node(df.loc[ind,'w'],ind)
        node_sequence.append(node)
    root = Haffuman_tree(node_sequence)
    Huffman_encoding(node_sequence,root)
