#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-25
'''
定义一个温度类，然后定义两个描述符用来描述摄氏度和华氏度两个属性
要求两个属性会自动进行转换，也就是说你可以给摄氏度这个属性赋值后打印出来的
为华氏度属性是自动转换后的结果。
'''
class Transverter():
    def __init__(self,fget,fset,fdel):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        return self.fset(instance,value)
    def __delete__(self, instance):
        return self.fdel(instance)

class Temperature():
    def __init__(self):
        self.fah = 0
        self.cen = 0

    def getCen(self):
        self.cen = (self.fah-32)/1.8
        return self.cen

    def getFah(self):
        self.fah = self.cen*1.8 +32
        return self.fah

    def setCen(self,value):
        self.cen = value

    def setFah(self,value):
        self.fah = value

    def delCen(self):
        del self.cen

    def delFah(self):
        del self.fah

    c = Transverter(getCen,setCen,delCen)

    f = Transverter(getFah,setFah,delFah)
