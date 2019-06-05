#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
把列表
member =  ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
使用insert()方法修改为下面的列表
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
'''
member =  ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
num = [88,90,85,90,88]
new_member = []

length = len(member)
for i in range(length):
    new_member.append(member[i])
    new_member.append(num[i])
member = new_member
print(member)