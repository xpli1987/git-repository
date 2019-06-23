#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-23
'''
定义一个类继承于 int 类型，并实现一个特殊功能：当传入的参数是字符串的时候，
返回该字符串中所有字符的 ASCII 码的和（使用 ord() 获得一个字符的 ASCII 码值）
'''
class New_int(int):
    def __new__(cls, n):
        str_n = str(n)
        num = 0
        if str_n.isdigit():
            num = n
            return int.__new__(cls,num)
        else:
            for index in range(len(str_n)):
                num += ord(str_n[index])
            return int.__new__(cls,num)

'''
class Nint(int):
        def __new__(cls, arg=0):
                if isinstance(arg, str):      #通过isinstance来判断arg为字符串
                        total = 0
                        for each in arg:
                                total += ord(each)
                        arg = total
                return int.__new__(cls, arg)
'''
