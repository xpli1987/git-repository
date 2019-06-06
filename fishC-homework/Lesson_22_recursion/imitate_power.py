#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
使用递归函数模拟power(x,y)函数。
power(x,y)函数为求x的y次幂的值
'''
def imitate_power(x,y):
    if y == 1:
        return x
    else:
        return x*imitate_power(x,y-1)

result = imitate_power(2,3)
print(result)