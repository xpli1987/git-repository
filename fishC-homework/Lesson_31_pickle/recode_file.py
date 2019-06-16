#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
把F:\学习资料\python\pickle\record.txt中的对话按照以下要求腌制成不同文件
小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”）
文件中总共有三段对话，分别保存为boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件
（提示：文件中不同的对话间已经使用“==========”分割）

解题思路：
1、把文件读取出来后按每行进行确认是“小甲鱼:”还是“小客服:”说的话，然后保存到列表中
2、如果该行为“==========”则进行分列表保存会话
3、三段会议通过两个“==========”进行分割
4、保存好的列表再通过pickle模块进行保存
'''
import pickle


def save_file(num,boy,girl):
    boy_filename = 'boy_' + str(num) + '.txt'
    girl_filename = 'girl' + str(num) + '.txt'
    with open('F:\\学习资料\\python\\pickle\\' + boy_filename, 'wb') as f_boy:
        pickle.dump(boy, f_boy)
    with open('F:\\学习资料\\python\\pickle\\' + girl_filename, 'wb') as f_girl:
        pickle.dump(girl, f_girl)

def main():
    num = 1
    boy_list = []
    girl_list = []
    with open(r'F:\学习资料\python\pickle\record.txt','r') as f:
        for each_line in f:
            if  "==========" in each_line:
                # print(each_line)
                # print(boy_filename)
                # print(girl_filename)
                save_file(num,boy_list,girl_list)
                boy_list = []
                girl_list = []
                num += 1
                print(num)
            else:
                each_line_list = each_line.split(':')
                if each_line_list[0] == '小甲鱼':
                    boy_list.append(each_line_list[1])
                    # print(each_line_list[1])
                elif each_line_list[0] == '小客服':
                    girl_list.append(each_line_list[1])
                    # print(each_line_list[1])
                # print(boy_list, girl_list)
        save_file(num,boy_list,girl_list)

if __name__ == '__main__':
    main()