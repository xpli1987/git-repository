#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
还原下面的列表推导式
list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
'''
list1 = []
for x in range(10):
    # if x%2 == 0:
    for y in range(10):
        if y%2 != 0 and x%2 == 0:
            list1.append((x,y))

print(list1)
