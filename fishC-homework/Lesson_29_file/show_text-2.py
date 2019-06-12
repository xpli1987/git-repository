#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
在show_text-1代码基础上进行优化：
1、用户可以要求显示指定行代码
2、输入格式如下：
    1）需要显示13到21行则输入13:21
    2）需要显示文件到第13行则输入:13
    3）需要显示21行到文件尾则输入21:
    4）如果需要显示的开始行数字大于文件行数则提示错误
    5）如果需要显示的结束行数字大于文件行数则显示开始行到文件尾
    6）如果输入结束行数字小于开始行数字则提示错误，要求重新输入
'''

def show_text(start,end,file_path='E:\\xpli\\123.txt'):
    with open(file_path) as f:
        file_list = list(f)
        length = len(file_list)
        if end == -1:
            print('文件%s第%d行到第%d行的内容如下：' % (file_path, start, length))
            for i in range(start - 1, length):
                print(file_list[i], end='')
        elif -1 < end < length:
            print('文件%s第%d行到第%d行的内容如下：'%(file_path,start,end))
            for i in range(start-1,end):
                print(file_list[i],end='')
        if start <= length < end:
            print('文件%s只有%d行！文件内容显示如下:'%(file_path,length))
            for i in range(start-1,length):
                print(file_list[i],end='')

def line_num(string):
    while True:
        str_list = string.split(':')
        # if str_list[0] == '':
        #     start_line_num = 0
        # else:
        #     start_line_num = int(str_list[0])
        start_line_num = 1 if str_list[0] == '' else int(str_list[0]) #三元操作符优化代码
        # if str_list[1] == '':
        #     end_line_num = -1
        # else:
        #     end_line_num = int(str_list[1])
        end_line_num = -1 if str_list[1] == '' else int(str_list[1])  #三元操作符优化代码
        if start_line_num <= end_line_num or end_line_num == -1:
            return start_line_num, end_line_num
        else:
            string = input('输入错误，请重新输入：')

def main():
    file_path = input('请输入要打开的文件(默认为E:\\xpli\\123.txt)')
    user_input = input('请输入需要显示该文件前几行：')
    start_line_num, end_line_num = line_num(user_input)
    if file_path == '':
        show_text(start_line_num,end_line_num)
    else:
        show_text(start_line_num,end_line_num,file_path)

if __name__ == '__main__':
    main()