#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
使用递归方法把十进制转换为二进制：
1、使用取商取余法转换
2、输出为字符串格式
3、使用递归函数
'''
def de_to_binary(n):
    if n == 0 or n == 1:
        binary_num = str(n)
    else:
        binary_num = de_to_binary(n//2)+str(n%2)
    return binary_num

# def Dec2Bin(dec):
#     result = ''
#
#     if dec:
#         result = Dec2Bin(dec // 2)
#         return result + str(dec % 2)
#     else:
#         return result


print(de_to_binary(62))
#
# n = 10
# print('0b'+de_to_binary(n))