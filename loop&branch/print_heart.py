#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
通过for循环来打印出心形图案
'''

def print_heart(x,y):
    for i in range(x,y+1):
        print(' '*(y+1-x))

