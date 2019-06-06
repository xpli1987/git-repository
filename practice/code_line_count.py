#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
统计目录C:\Users\460002000439\PycharmProjects下所有文件的代码行数：
1、只统计后缀为py的文件
2、只统计有效的代码行，也就是所有的注释行均认作无效代码
3、输出需要有py的文件数及各文件名对应的代码行数
4、输出总的代码行数
'''
from time import sleep
import os

#初始化相关数据
dir_init = r'C:\Users\460002000439\PycharmProjects\'  #待统计代码行数的初始目录
code_line_num = 0 #初始化代码行数
each_py_num = {} #初始化Python文件对应的代码行数字典

