#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
显示目录下所有文件大小：
解题思路：
1、要使用os.path.getsize(file)方法来获取文件的大小
2、需要获取文件的路径，可以通过os.walk返回的三元组中的第1个元素与第3个元素进行组合来获取
3、因为显示时只需要文件名和大小，所以os.walk返回的三元组中的第3个元素需要进行保存
4、最终需要显示文件名和大小，所以可以用字典来保存文件名和大小
'''

#导入os,和os.path路径
import os,os.path

def get_file_path(dir_path):
    #通过列表推导式和os.walk(path)方法获取一个存储文件路径的列表
    file_path = [each[0]+'\\'+ each_element for each in os.walk(dir_path) if len(each[2]) !=0 for each_element in each[2]]
    # for each in os.walk(dir_path):
    #     if len(each[2]) != 0:
    #         for each_element in each[2]:
    #             file_path.append(each[0]+'\'+each_element)
    return file_path

def get_file_size(file):
    #建立一个字典用来存储文件名及文件对应的大小
    file_size = dict()
    for each_file in file:
        #通过每个文件的绝对路径使用os.path.getsize(file)方法来获取大小
        size_of_file = os.path.getsize(each_file)
        #通过os.path.basename(path)来获取文件名作为字典的key
        file_size[os.path.basename(each_file)] = size_of_file
    return file_size

def main():
    dir_path = input('请输入需要显示目录下所有文件大小的路径：')
    file_path = get_file_path(dir_path)
    file_size = get_file_size(file_path)
    for each_key in file_size.keys():
        print(each_key,'【%dBytes】' % file_size[each_key])

if __name__ == '__main__':
    main()