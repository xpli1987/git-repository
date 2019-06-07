#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
通过递归方法分解一个整数的各个位数字到列表中
1、使用递归方法
2、所12345分解返回为[1,2,3,4,5]
'''
num_list = []
def get_digits(n):
    if n >= 10:
        num_list.insert(0,n % 10)
        get_digits(n // 10)
    else:
        num_list.insert(0,n)


get_digits(12345)
print(num_list)