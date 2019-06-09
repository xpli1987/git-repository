#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
编写一个符合下面要求的函数：
a) 计算打印所有参数的和乘以基数（base=3）的结果
b) 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算。
需求分解：
1、函数需要有收集参数，默认参数
2、对收集参数的所有参数进行求和，然后与基数相乘
3、最后一个关键字参数不参数求和
'''

def argu_sum(*num, base=3):
    num_sum = 0
    for each in num:
        num_sum += each
    return num_sum*base

print(argu_sum(1,2,3,4,5,6,7))
print(argu_sum(1,2,3,4,5,6,7,base=5))


