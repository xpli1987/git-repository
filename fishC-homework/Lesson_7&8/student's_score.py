#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
把输入的成绩转换为A,B,C,D的级别：
按照 100 分制，90 分以上成绩为 A，80 到 90 为 B，60 到 80 为 C，60 以下为 D
'''

score_str = input('请输入学生的成绩：')
print(int(score_str))

while not score_str.isdigit() or int(score_str)>100 or int(score_str)<0:
    score_str = input("输入错误，请重新输入：")

score = int(score_str)

if 60 <= score < 80:
    print('该同学的成绩为C')
elif 80 <= score < 90:
    print("该同学的成绩为B")
elif score >= 90:
    print("该同学成绩为A")
else:
    print("该同学需要辅导，成绩为D")