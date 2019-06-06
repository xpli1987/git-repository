#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
使用递归函数求n的阶乘：
1*2*3*...*n
'''
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

n = 5
x = factorial(n)
print(x)