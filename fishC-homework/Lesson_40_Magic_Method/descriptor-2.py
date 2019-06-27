#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-26
'''
编写描述符 MyDes，使用文件来存储属性，属性的值会直接存储到对应的pickle
（腌菜，还记得吗？）的文件中。如果属性被删除了，文件也会同时被删除，属性
的名字也会被注销
'''
import pickle as p
import os

class MyDes:
    def __init__(self,name,value=0):
        self.name = name
        self.value = value
        self.file_path = r'E:\xpli\git\descriptor'
        self.file_name = self.name + '.pkl'

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
        os.chdir(self.file_path)
        with open(self.file_name,'wb') as f:
            p.dump(self.value,f)

    def __delete__(self, instance):
        del self.name
        os.chdir(self.file_path)
        os.remove(self.file_name)

class Test:
    x = MyDes('x')
    y = MyDes('y')