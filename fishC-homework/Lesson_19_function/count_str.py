#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
统计下边路径文件中的长字符串中各个字符出现的次数并找到小甲鱼送给大家的一句话
path = r'F:\学习资料\python\function\string1.txt'
'''

def count_str(string):
    tmp = list(set(string))
    str_dict = dict()
    str_list = []
    #统计各个字符出现的次数
    for each in tmp:
        str_dict[each] = string.count(each)
        each_str = str(each)
    #找出小甲鱼送给大家的话
    for x in string:
        if x.isalpha():
            str_list.append(x)
    return str_dict,str_list

with open(r'F:\学习资料\python\function\string1.txt','r') as f:
    string = f.read()
    count_dict,str_list = count_str(string)
    for key in count_dict.keys():
        print(key,'->',count_dict[key])
    for each in str_list:
        print(each)