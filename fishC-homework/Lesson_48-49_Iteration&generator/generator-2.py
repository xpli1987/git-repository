#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-29
'''
10 以内的素数之和是：2 + 3 + 5 + 7 = 17，那么请编写程序，计算 2000000 以内的素数之和
'''
import math
# def is_prime(number):
#     if number > 1:
#         if number == 2:
#             return True
#         if number % 2 == 0:
#             return False
#         for current in range(3, int(math.sqrt(number) + 1), 2):
#             if number % current == 0:
#                 return False
#         return True
#     return False
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def primes(num_max):
    num = 2
    while num <= num_max:
        if is_prime(num):
            yield num
        num += 1

# sum_num = 0
# for i in primes(2000000):
#     sum_num += i
#
# print(sum_num)
print(sum(primes(2000000)))
# print(sum(num for num in range(2000000) if is_prime(num)))
