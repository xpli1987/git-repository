#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上
'''

def show_text(line_num,file_path='E:\\xpli\\123.txt'):
    with open(file_path) as f:
        file_list = list(f)
        length = len(file_list)
        if line_num <= length:
            print('文件%s的前%d的内容如下：'%(file_path,line_num))
            for i in range(line_num):
                print(file_list[i],end='')
        if line_num > length:
            print('文件%s只有%d行！文件内容显示如下:'%(file_path,length))
            for i in range(length):
                print(file_list[i],end='')

def main():
    file_path = input('请输入要打开的文件(默认为E:\\xpli\\123.txt)')
    line_num = int(input('请输入需要显示该文件前几行：'))
    if file_path == '':
        show_text(line_num)
    else:
        show_text(line_num,file_path)

if __name__ == '__main__':
    main()