#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#_*_ ThunderRuss_XPLI
'''
定义一个点（Point）类和直线（Line）类，使用 getLen 方法可以获得直线的长度。
提示：
设点 A(X1,Y1)、点 B(X2,Y2)，则两点构成的直线长度 |AB| = √((x1-x2)2+(y1-y2)2)
Python 中计算开根号可使用 math 模块中的 sqrt 函数
直线需有两点构成，因此初始化时需有两个点（Point）对象作为参数
'''
import math

#定义一个点类
class Point():
    #点有坐标由x,y轴坐标构成
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


#定义一个线类：线由两个点构成，所以可以继承点类
class Line():
    def __init__(self,p1,p2):
        self.x = p1.getX() - p2.getX()
        self.y = p1.getY() - p2.getY()
        self.len = math.sqrt(self.x**2 + self.y**2)

    def getlength(self):
        return self.len

p1 = Point(1,1)
p2 = Point(4,5)

line = Line(p1,p2)

print(line.getlength())