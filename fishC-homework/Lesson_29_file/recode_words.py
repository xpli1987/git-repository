#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
 编写一个程序，接受用户的输入并保存为新的文件:
 1、接收用户的输入
 2、用户输入内容保存为一个新的文件
 3、输入':w'时退出程序
'''

#定义一个用户保存文件名的输入变量file_name
file_name = input('请输入文件名：')

def recode_words():
    # 定义一个存储用户输入内容的列表变量words_list
    words_list = []
    user_words = input('请输入内容【单独输入":w"保存退出】:')
    while True:
        if user_words == ':w':
            break
        else:
            words_list.append(user_words + '\n')
            user_words = input()
    return words_list

user_words_list = recode_words()
with open(file_name,'w') as f:
    f.writelines(user_words_list)
