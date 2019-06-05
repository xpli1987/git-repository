#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
打印乘法表
'''
for x in range(1,10):
    for y in range(1,x+1):
        if x==y:
            print("%d*%d=%d"%(x,y,x*y),end='\n')
        else:
            print("%d*%d=%d"%(x,y,x*y),end=' ')