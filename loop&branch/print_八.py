#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
通过打印*号组成一个“八”字
'''
n = 17
for x in range(1,(n+1)//3+1):
    print(" "*((n+1)//3-x)+"*"+" "*(n-((n+1)//3-x)*2-2)+"*"+" "*((n+1)//3-x))