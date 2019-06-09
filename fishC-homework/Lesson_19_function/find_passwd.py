#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
找出字符串"ABSaDKSbRIHcRHGcdDIF"中的密码
a) 每位密码为单个小写字母
b) 每位密码的左右两边均有且只有三个大写字母j
'''

string = 'ABSaDKSbRIHcRHGcdDIF'
length = len(string)
passwd = []
for i in range(3,length-4):
    if string[i].islower():
        if string[i-3].isupper() and string[i-2].isupper() and string[i-1].isupper():
            if string[i+3].isupper() and string[i+2].isupper() and string[i+1].isupper():
                passwd.append(string[i])

for each in passwd:
    print(each,end='')