#!/usr/bin/evn python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索.
解题思路：
第一种方案：使用os.walk(path)方法
1、把用户输入的文件名在os.walk(path)返回列表中每一个三元组中第三个元素进行对比，如果存在则返回三元组中的路径和文件名
2、如果不存在则返回None
'''
import os,os.path

def search_file(path,filename):
    exist_path = [each[0] + os.sep + filename for each in os.walk(path) if filename in each[2]]
    # for each in os.walk(path):
    #     if filename in each[2]:
    #         exist_path.append(each[0] + os.sep + filename)
    return exist_path

def main():
    search_path = input('请输入待查找的初始目录：')
    target_filename = input('请输入待查找的文件名：')
    file_path = search_file(search_path,target_filename)
    for each_path in file_path:
        print(each_path)

if __name__ == '__main__':
    main()