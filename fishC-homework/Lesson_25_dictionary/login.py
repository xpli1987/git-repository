#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
编写一个登录程序：
1、用户输入指令N/n则新建用户
2、用户输入指令E/e则登录账号
3、用户输入指令Q/q则退出程序
'''

#新建一个字典用来存储用户信息
info_dict = dict()

msg = \
'''
|--- 新建用户：N/n  ---|
|--- 登录账号：E/e  ---|
|--- 退出程序：Q/q  ---|
|--- 请输入指令代码：
'''

#新建用户
def add_user(name):
    while True:
    # 判断用户名是否被使用
        if not info_dict.get(name):
            passwd = input('请输入密码：')
            info_dict[name] = passwd
            break
        else:
            name = input('此用户名已经被使用，请重新输入：')
    print('注册成功，赶紧试试登录吧^_^',end='\n\n')

#登录账号
def login_id(name):
    # 判断用户名是否存在
    while True:
        if not info_dict.get(name):
            name = input('您输入的用户名不存在，请重新输入：')
        else:
            break
    passwd = input('请输入密码：')
    #验证密码是否正确
    while True:
        if info_dict[name] == passwd:
            print('欢迎进入系统，可点击右上角的‘X’结束程序！',end='\n\n')
            break
        else:
            passwd = input('输入密码错误，请重新输入：')


def main():
    while True:
        user_order = input(msg)
        while True:
            if user_order.upper() not in ('N', "E", 'Q'):
                user_order = input('输入错误指令，请重新输入：')
            else:
                break
        if user_order.upper() == 'Q':
            print('欢迎您再次使用本程序！！！')
            break
        else:
            name = input('请输入用户名：')
            if user_order.upper() == 'N':
                add_user(name)
            else:
                login_id(name)

if __name__ == '__main__':
    main()