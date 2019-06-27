#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-26
'''
按要求编写描述符 MyDes：当类的属性被访问、修改或设置的时候，分别做出提醒
'''
class MyDes:
    def __init__(self,value=0,name=0):
        self.value = value
        self.name = name

    def __get__(self, instance, owner):
        print('正在获取变量：',self.name)
        return self.value

    def __set__(self,instance,value):
        print('正在修改变量：',self.name)
        self.value = value

    def __delete__(self, instance):
        print('正在删除变量：',self.name)
        print('哦，这个变量无法删除')

class Test:
    x = MyDes(10,'x')