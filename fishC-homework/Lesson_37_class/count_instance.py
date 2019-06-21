#!usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
在一个类中定义一个变量，用于跟踪该类有多少个实例被创建（当实例化一个对象，这个变量+1，当销毁一个对象，这个变量自动-1）
解题思路：
需要了解类对象，实例对象及self的作用。
类属性：
静态变量，通常用来跟踪与类相关的值
实例属性：
在方法中通过self来指向的属性
'''

class C():
    num = 0  #这是一个类属性，用来跟踪类相关的值
    def __init__(self):   #实例化类时自动被调用
        C.num += 1    #表示如果类被实例批了则类属性num自动+1

    def __del__(self):    #删除实例对象时自动被调用
        C.num -= 1    #表示如果实例对象被删除时类属性num自动-1

#通过上面的类属性num我们可以来统计创建了多少个实例
print(C.num)
c = C()
print(C.num)
a = C()
print(C.num)
b = C()
print(C.num)

del a,b
print(C.num)
