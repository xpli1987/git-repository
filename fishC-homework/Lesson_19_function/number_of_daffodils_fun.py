#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
找出所有水仙花数：
水仙花数定义：
如果一个三位数的个、十、百位的立方和等于该数则称为水仙花数，如153=1**3 + 5**3 +3**3
'''
def num_of_daffodils():
    num_list = []
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                if c * 100 + b * 10 + a == c ** 3 + b ** 3 + a ** 3:
                    num = c * 100 + b * 10 + a
                    num_list.append(num)
    return num_list

for each in num_of_daffodils():
    print(each)