#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
把下面两个列表：
list1 = ['1.Just do It', '2.一切皆有可能','3.让编程改变世界','4.Impossible is Nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
用推导式组合成另外一个列表：
list3 = ['1.耐克:Just do It','2.李宁:一切皆有可能','3.鱼C工作室:让编程改变世界','4.阿迪达斯:Impossible is Nothing']
'''
list1 = ['1.Just do It', '2.一切皆有可能','3.让编程改变世界','4.Impossible is Nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']

list3 = [(y+':'+x[2:]) for x in list1 for y in list2 if x[0:2] == y[0:2]]

for element in list3:
    print(element)