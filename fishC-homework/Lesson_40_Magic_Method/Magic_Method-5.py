#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-23
'''
定义一个新的类 Nstr，也支持移位操作符的运算
'''
class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[0:other]

    def __rshift__(self, other):
        return self[-other:] + self[:-other]