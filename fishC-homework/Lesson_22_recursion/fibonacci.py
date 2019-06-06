#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
用递归方法构造Fibonacci数据模型
'''
# def fibonacci(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# fibonacci_num = fibonacci(20)

#用迭代方法构造Fibonacci数据模型
def fibonacci(n):
    num = 1
    if n <= 2:
        return num
    else:
        for i in range(1,n-2):
            num = 1 + i**(i-1)

print(fibonacci_num)