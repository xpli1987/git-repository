#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunerRuss_XPLI
#__DATE__:2019-06-23
'''
写一个 FileObject 类，给文件对象进行包装，从而确认在删除对象时文件能自动关闭
'''

class FileObject():
    def __init__(self,path,mode):
        self.path = path
        # print(self.path)
        self.mode = mode
        # print(self.mode)
        #
    def open(self):
        self.f = open(self.path, self.mode)

    # def read(self,size=-1):
    #     print(self.f.read(size))
    #
    # def write(self,string):
    #     self.f.write(string)

    def __del__(self):
        print('__del__方法被调用了...')
        self.f.close()
        del self.f

#代码验证
a = FileObject(r'f:\sublime证书.txt','a')
a.open()
a.write('\n543243324')
# a.write('54352345')