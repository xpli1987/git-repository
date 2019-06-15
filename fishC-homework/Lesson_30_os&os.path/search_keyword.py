#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含
有该关键字的文本文件（.txt后缀），要求显示该文件所在的位置以及关键字在文件中的具体位置（第
几行第几个字符）
两种解题思路：
一、os.walk()方法
二、递归方法
本代码使用第一种方法：
代码思路：
1、使用walk方法把所有文件路径存放到列表中
2、使用for循环语句判断关键字是否在文件中
3、在文件中则确认关键字所在行数和第几个字并以元组方式返回
4、把关键字所在文件路径及位置元组保存到字典中
'''

import os

def find_file(path):
    file_list = []
    for each in os.walk(path):
        if len(each[2]) != 0:
            # print(each[0])
            #file_list存放文件路径，用列表推导式把文件以列表形式到file_list
            for each_file in each[2]:
                if os.path.splitext(each_file)[1] == '.txt':
                    if each[0] == 'f:\\':
                        file_list.append(each[0] + each_file)
                        # print(each[0] + each_file)
                    else:
                        file_list.append(each[0] + os.sep + each_file)
                        # print(each[0] + os.sep + each_file)
                    # print(each[0])
    # print(file_list)
    return file_list

def keyword_position(file_path,keywords):
    line_num = 0
    word_position = dict()
    file_word_position = []
    for each_path in file_path:
        # print(each_path)
        with open(each_path, 'r',encoding='utf-8',errors='ignore') as f:
            if keywords in f.read():
                f.seek(0, 0)
                for each_line in f:
                    line_num += 1
                    if keywords in each_line:
                        position_list = find_index(each_line,keywords)
                        # print(position_line)
                        file_word_position.append((line_num,position_list))
                word_position[each_path] = file_word_position
        file_word_position = []

    # print(word_position)
    return word_position

def find_index(string,keyword):
    position_list = []
    position_index = 0
    while True:
        if string.index(keyword) != string.rindex(keyword):
            position_index += string.index(keyword)
            position_list.append(position_index)
            string = string[string.index(keyword) + 3:]
            position_index += 3
        else:
            position_index += string.index(keyword)
            position_list.append(position_index)
            break
    return position_list




def main():
    start_path = input('请输入要查找的目录：')
    keywords = input('请输入待查找的关键字：')
    # print(keywords)
    file_path = find_file(start_path)
    keywords_position = keyword_position(file_path,keywords)
    print('正在保存关键字位置')
    for each_key in keywords_position.keys():
        # print(each_key)
        print('在文件【%s】中找到关键字【%s】' %(each_key,keywords))
        for each in keywords_position[each_key]:
            print('关键字出现在第%d行，第'%each[0],each[1],'的位置')

if __name__ == '__main__':
    main()