#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
通过for循环打印下面的列表元素
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
打印结果要求如下：
小甲鱼 88
黑夜 90
迷途 85
怡静 90
秋舞斜阳 88
'''
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
length = len(member)

for i in range(0,length,2):
    print(member[i] + ' ' + str(member[i+1]))

