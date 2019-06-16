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
本代码使用第二种方法：
解题思路：
1、通过递归方法把目录下所有txt文件的绝对路径存放到列表返回
2、确认关键字在txt文件中并返回文件所在行和该第多少个字
3、某行有多个关键字需要全部返回到列表中
'''
import os,time

txt_list = []
def search_ext(path,ext):
    #进入目标目录
    os.chdir(path)
    #当前目录下所有文件存入到列表中
    file_list = os.listdir(os.curdir)
    #对列表中的文件进行判断是文件还是目录
    for each_file in file_list:
        # print(each_file)
        #如果是文件
        if os.path.isfile(each_file):
            # print('这是个文件')
            if os.path.splitext(each_file)[1] == ext:
                #判断当前目录是否为win磁盘根目录，比如f:\盘，如果是os.getcwd()返回的为f:\\，不是则返回的是f:\\工作
                if os.getcwd()[2:] == '\\':
                    txt_list.append(os.getcwd()+each_file)
                else:
                    txt_list.append(os.getcwd() + os.sep + each_file)
        #如果是盘符‘System Volume Information’或者回收站“$RECYCLE.BIN”
        elif each_file == 'System Volume Information' or each_file == '$RECYCLE.BIN':
            pass
        else:
            # print('这是个目录')
            search_ext(each_file,ext)
            os.chdir(os.pardir)

#在一个字符串里面查找关键字并返回所有关键字位置
def find_keyword_instring(string,keyword):
    #keyword_position用于存放关键字位置
    keyword_position = []
    #用while循环来重复获取关键字位置
    while True:
        #如果关键字从左边开始查找和从右边开始查找的索引相等，则表示该string中只包含一个关键字
        if string.index(keyword) == string.rindex(keyword):
            keyword_position.append(string.index(keyword))
            break
        else:
            #如果不相等，把第一个关键字位置索引存入到列表
            keyword_position.append(string.index(keyword))
            #字符串保留关键字出现后的部分并保存到string变更中方便下次调用
            string = string[(string.index(keyword) + len(keyword)):]
    return keyword_position

#在文件中查找所有行的关键字位置
def find_keyword_infile(file,keyword):
    #file_position用来记录关键字在文件中的位置，列表的每一个元素包括关键字所在行和位置的元组
    file_position = []
    #num用来记录文件所在行数，初始为0
    num = 0
    #以只读方式打开文件，文件以utf-8的编码方式打开，如果发生错误则忽略
    with open(file,'r',encoding='utf-8',errors='ignore') as f:
        #判断文件中是否包含关键字
        if keyword in f.read():
            #因之前读取了文件，文件指针已经移动到了文件末尾，所以需要把指针移动到文件开始
            f.seek(0,0)
            #对文件的每一行进行查找是否存在关键字，如果存在则返回所在行第几个字
            for each_line in f:
                #每进入一行num需要加1
                num += 1
                if keyword in each_line:
                    line_position = find_keyword_instring(each_line,keyword)
                    file_position.append((num,line_position))
    return file_position


#程序运行
def main():
    #字典keyword_position用来存放关键字所在位置，key为文件所在位置，value为保存关键字所在行和位置的列表
    keyword_position = dict()
    init_path = input('请输入要查找的初始目录：')
    file_ext = input('请输入在哪种文件类型中查找：')
    keyword = input('请输入要查找的关键字：')
    search_ext(init_path,file_ext)
    for each_file in txt_list:
        file_position = find_keyword_infile(each_file,keyword)
        keyword_position[each_file] = file_position
    for each_key in keyword_position.keys():
        if keyword_position[each_key]:
            print('在文件【%s】中找到关键字【%s】' %(each_key,keyword))
            for each_line in keyword_position[each_key]:
                print('关键字出现在第%d行，第' % each_line[0],each_line[1],'个位置。')

if __name__ == '__main__':
    print(time.ctime())
    main()
    print(time.ctime())

'''
通过打印ctime时间发现递归会比使用os.walk(path)函数慢将近20s
所以建议在不必要情况下不使用递归方法
'''