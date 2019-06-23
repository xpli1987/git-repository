#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-23
'''
定义一个类实现摄氏度到华氏度的转换（转换公式：华氏度 = 摄氏度*1.8+32）
'''

class C2F():
    def __init__(self,c):
        self.c = c
        self.f = self.c * 1.8 + 32

    def __str__(self):
        return str(self.f)

    def __repr__(self):
        return str(self.f)

#验证代码
C2F(32)
print(C2F(32))
