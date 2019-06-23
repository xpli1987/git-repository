#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-23
'''
定制一个定时器，要求满足如下需求：
1、两个计时器可以相加
2、能够直接显示timer
'''
import time

class MyTimer():
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.last = []
        self.unit = ['年','月','天','小时','分钟','秒']
        self.prompt = '未开始计时!'
        self.tmp = []

    def start(self):
        print('计时开始...')
        self.begin = time.localtime()

    def stop(self):
        if self.begin:
            self.end = time.localtime()
            print('计时结束...')
            for index in range(6):
                self.last.append(self.end[index] - self.begin[index])
            for index in range(6):
                if self.last[index]:
                    self.tmp.append(str(self.last[index])+self.unit[index])
            self.prompt = '总共运行了' + ''.join(self.tmp)
            self.tmp = []
        else:
            print('提示：请先调用start()开始计时！')

    def __repr__(self):
        return self.prompt

    def __str__(self):
        return self.prompt

    def __add__(self, other):
        for index in range(6):
            if self.last[index] + other.last[index]:
                self.tmp.append(str(self.last[index] + other.last[index])+self.unit[index])
        self.prompt = '总共运行了' + ''.join(self.tmp)
        return self.prompt

