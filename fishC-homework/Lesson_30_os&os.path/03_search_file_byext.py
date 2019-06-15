#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件（要求查找mp4 rmvb, avi的格式即可），
并把创建一个文件（vedioList.txt）存放所有找到的文件的路径.
因为对递归函数不够熟悉，所以本代码仍然使用递归函数实现：
解题思路：
1、进入目录路径
2、通过os.listdir(path)把目录下所有文件和目录使用列表存储
3、把所有文件后缀名与文件名分割开，并把后缀名与目标文件后缀名进行比较
4、属于目标文件则把文件绝对路径存放到列表中
5、如果是目录则递归调用函数
'''
import os,os.path
target_file_path = []

def search_file_extname(path,target):
    os.chdir(path)
    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            print('我是一个文件：%s' %each_file)
            target_file_path.append(path+os.sep+each_file+os.linesep)
        if os.path.isdir(each_file):
            print('我是一个目录：%s' % each_file)
            search_file_extname(each_file,target)
            os.chdir(os.pardir)

def main():
    init_path = input('请输入查找初始路径：')
    target_ext_list = ['.avi','.mp4','.rmvb']
    search_file_extname(init_path,target_ext_list)
    print(target_file_path)
    with open(r'e:\xpli\target_file_path.txt','w') as f:
        for each_file_path in target_file_path:
            f.writelines(each_file_path)
    print('已经全部查找完成，文件路径已经存放到e:\\xpli\\target_file_path.txt中！')

if __name__ == '__main__':
    main()