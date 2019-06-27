#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-26
'''
按要求编写描述符 MyDes：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件：record.txt
'''
import time as t
import os

class Record:
    def __init__(self,value=0,name=0):
        self.value = value
        self.name = name
        self.file_path = r'E:\xpli\record.txt'

    def _log(self,option='get'):
        with open(self.file_path,'a') as f:
            self.times_stamp = t.ctime()
            if option == 'get':
                self.logs = '获取属性%s的值%s' %(self.name,str(self.value))
            elif option == 'set':
                self.logs = '设置属性%s的值%s' % (self.name, str(self.value))
            else:
                self.logs = '删除属性%s' % self.name
            f.write(self.times_stamp + ':  '+self.logs + os.linesep)

    def __get__(self, instance, owner):
        self._log('get')
        return self.value

    def __set__(self, instance, value):
        self.value = value
        self._log('set')

    def __delete__(self, instance):
        del self.name
        self._log('del')

class Test:
    x = Record(10,'x')
    y = Record(8.8,'y')