#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-28
'''
要求自己写一个 MyRev 类，功能与 reversed() 相同（内置函数 reversed(seq) 是返回一个迭代器，是序列 seq 的逆序显示）
'''
# class MyRev:
#     def __init__(self,seq):
#         self.seq = reversed(seq)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self.seq)


#真正在实现reversed()函数功能
class MyRev:
    def __init__(self,seq=0):
        self.seq = seq
        self.index = len(self.seq)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.seq[self.index]
        else:
            raise StopIteration