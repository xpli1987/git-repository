#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内
1、用户有三次输入错误密码机会
2、如果输入的密码包含有“*”则不计算在三次机会里面
'''

password = input('请输入你的密码：')
true_password = 'lxp@19870204'
num = 3

while '*' in password:
    password = input('密码中不能包含“*”号，你还有3次机会，请重新输入密码：')

while not num == 0:
    if password == true_password:
        print('密码正确，进入程序...')
        break
    else:
        num -= 1
        if num == 0:
            print('对不起，您已经超过密码输入次数，请重新运行密码后输入！')
        else:
            password = input('密码输入错误！您还有%d次机会！请输入密码：'%num)