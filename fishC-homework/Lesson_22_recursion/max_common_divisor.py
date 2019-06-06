#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
用递归函数求最大公约数。
公约数就是能同时被多个整数整除的整数，1是所有整数的公约数
'''
##普通函数实现求最大公约数
# def max_common_divisor(x,y):
#     result = 1
#     min_num = min(x,y)
#     num_list = [i for i in range(1,min_num) if x%i==0 and y%i==0 and i>result]
#     result = num_list[0]
#     return result

#使用欧几里德算法，也叫辗转相除法
def max_common_divisor(x,y):
    if y:
        return max_common_divisor(y,x%y)
    else:
        return y
num = max_common_divisor(12,15)
print(num)