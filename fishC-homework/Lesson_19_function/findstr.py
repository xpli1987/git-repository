#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
统计一个长度为 2 的子字符串在另一个字符串中出现的次数。
需求分析：
1、有两个字符串，一个长字符串，一个长度只有2的子字符串
2、统计长字符串中出现过多少次子字符串
'''

def findstr(string,sub_str):
    count_num = 0
    length = len(string)
    for i in range(length-1):
        if string[i]+string[i+1] == sub_str:
            count_num += 1
    return count_num

string = input('请输入目标字符串：')
sub_str = input('请输入子字符串：')
print(findstr(string,sub_str))