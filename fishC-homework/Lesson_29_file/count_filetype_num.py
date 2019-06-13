#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__ThunderRuss_XPLI
'''
统计当前目录下（包含子目录）所有文件类型的数量
解题思路：
1、获取当前目录下所有文件名
2、通过os.path.splitext()方法把文件名和文件扩展名区分开
3、根据文件扩展名进行统计各文件类型的数量
'''

import os,os.path

#获取当前目录下所有文件名
def get_filename(filename):
    file_list = list() #建立一个空的列表用来添加文件名
    file_walk = os.walk(filename) #使用os.walk()方法把目录路径，目录及文件名以一个三元祖形式返回
    for each in file_walk:
        if len(each[2]) != 0:
            file_list.extend(each[2])
    print(file_list)
    return file_list


#装有文件名的列表通过os.path.splitext()方法来分割出来扩展名并统计文件类型数量
def count_filetype(file_list):
    filetype_dict = dict()  #创建一个字典用来存储文件扩展名对应的数量
    for each in file_list:
        ext_list = os.path.splitext(each)  #把文件名分割成文件名+扩展名存入列表ext_list
        print(ext_list)
        if filetype_dict.get(ext_list[1]):   #如果扩展名在字典中，则扩展名对应字典的value值+1
            filetype_dict[ext_list[1]] += 1
        else:                            #如果扩展名不在字典中，则创建一个以扩展名为key，1为value的iterm
            filetype_dict[ext_list[1]] = 1
    # print(filetype_dict)
    return filetype_dict

def main():
    file_name = input('请输入需要统计文件类型数量的目录：')
    file_list = get_filename(file_name)
    filetype_dict = count_filetype(file_list)
    for eachkey in filetype_dict.keys():
        print('该文件夹下共有类型【%s】的文件%d个' %(eachkey,filetype_dict[eachkey]))

if __name__ == '__main__':
    main()