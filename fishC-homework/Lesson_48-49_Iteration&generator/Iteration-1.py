#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-28
'''
写一个迭代器，要求输出至今为止的所有闰年
'''

class LeapYear:
    def __init__(self,this=2019,begin= 0):
        self.this_year = this

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.this_year -= 1
            if self.this_year > 0:
                if not self.this_year % 4 and self.this_year % 100:
                    return self.this_year
                elif not self.this_year % 400:
                    return self.this_year
            else:
                raise StopIteration