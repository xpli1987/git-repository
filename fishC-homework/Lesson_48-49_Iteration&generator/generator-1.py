#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-29
'''
要求实现一个功能与 reversed() 相同（内置函数 reversed(seq) 是返回一个迭代器，是序列 seq 的逆序显示）的生成器
'''
def myrev(seq):
    length = len(seq) - 1
    while length >= 0:
        yield seq[length]
        length -= 1

for i in myrev('ThunderRuss_XPLI'):
    print(i,end='')

