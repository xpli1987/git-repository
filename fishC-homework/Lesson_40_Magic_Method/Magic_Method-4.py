#!/usr/bin/env python
#_*_ coding;utf-8 _*_
#__author__:ThunerRuss_XPLI
#__DATE__:2019-06-23
'''
要求定义一个 Nstr 类，支持字符串的相减操作：A – B，从 A 中去除所有 B 的子字符串
'''
class Nstr(str):
    def __sub__(self, other):
        return self.replace(other,'')