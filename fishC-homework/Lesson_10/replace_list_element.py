#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
把下面列表中的‘小甲鱼’替换为‘小鱿鱼’
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
'''
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1[1].pop()
list1[1].append(['小鱿鱼'])

print(list1)