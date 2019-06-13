#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索.
解题思路：
第二种方案：使用递归方法
1、进入当前目录，确认目录下文件是目录还是文件
2、是目录则进入该目录，确认该目录下文件是目录还是文件
3、是文件则确认是否为被查找文件
4、是被查找文件则存放到目标文件列表中
5、不是被查找文件则确认下一个文件是否为目标文件
'''
import os,os.path

def search_file(path,filename):
    os.chdir(path)
    fileindir = os.listdir(os.curdir)
    for each_file in fileindir:
        if os.path.isfile(each_file):
            if each_file == filename:
                print(path + os.sep + filename)
                # return [path + os.sep + filename]
        else:
            search_file(each_file, filename)
            os.chdir(os.pardir)


def main():
    file_path = input('请输入路径：')
    target_filename = input('请输入文件名：')
    search_file(file_path,target_filename)
    # for each in target_path:
    #     print(each)

if __name__ == '__main__':
    main()