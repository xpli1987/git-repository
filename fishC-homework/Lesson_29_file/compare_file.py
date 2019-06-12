#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
比较两个文件，如果不同则显示不同之处所在行数及不同的字符所在位置
1、统计有多少处不同之处
2、返回不同之处所在行号
3、返回不同之处开始的字符位置
思路：
1、两个文件行数一样
    1）统计有多少处不同之处
    2）返回不同之处所在行号
    3）返回不同之处开始的字符位置
2、两个文件行数不一样
    1）多的行数内容需要显示
    2）其它同场景1
'''


#打开两个文件
f1 = open(r'E:\xpli\123.txt','r')
f2 = open(r'E:\xpli\345.txt','r')

#定义一个字典存储不同行及内容不同字符位置
file_list = []

f1_list = list(f1)
f2_list = list(f2)
f1_length = len(f1_list)
f2_length = len(f2_list)

if f1_length == f2_length:
    for i in range(f1_length):
        if f1_list[i] != f2_list[i]:
            file_list.append(i+1)
else:
    if f1_length > f2_length:
        for i in range(f2_length):
            if f1_list[i] != f2_list[i]:
                file_list.append(i+1)
        for i in range(f2_length,f1_length):
            file_list.append(i+1)
    else:
        for i in range(f1_length):
            if f1_list[i] != f2_list[i]:
                file_list.append(i+1)
        for i in range(f1_length, f2_length):
            file_list.append(i+1)

f1.close()
f2.close()
print('两个文件共有【%d】处不同：' %len(file_list))
for each in file_list:
    print('第%d行不一样' %each)