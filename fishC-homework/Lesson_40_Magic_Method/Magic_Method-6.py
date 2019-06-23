#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-23
'''
定义一个类 Nstr，当该类的实例对象间发生的加、减、乘、除运算时，将该对象的所有字符串的 ASCII 码之和进行计算
'''
class Nstr(int):
    def __new__(cls, *args, **kwargs):
        total = 0
        for each in arges[0]:
            total += ord(each)
        return int.__new__(cls,total)
    #
    # def __add__(self, other):
    #     return self.total + other.total
    #
    # def __sub__(self, other):
    #     return self.total - other.total
    #
    # def __mul__(self, other):