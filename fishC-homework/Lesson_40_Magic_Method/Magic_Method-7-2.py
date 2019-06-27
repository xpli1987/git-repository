#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-23
'''
定制一个定时器，要求满足如下需求：
1、两个计时器可以相加
2、能够直接显示timer
在上个例子基础上进行改进：
如果开始计时的时间是（2022年2月22日16:30:30），
停止时间是（2025年1月23日15:30:30），那按照我们
用停止时间减开始时间的计算方式就会出现负数，应该对此做一些转换
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
            self._calc()
        else:
            print('提示：请先调用start()开始计时！')

    def _calc(self):
        self.begin.reverse()
        self.end.reverse()
        for index in range(6):
            if self.end[index] - self.begin[index] >= 0:
                self.last.insert(0, self.end[index] - self.begin[index])
            else:
                if index <= 1:
                    self.last.insert(0, 60 + self.end[index] - self.begin[index])
                elif index == 2:
                    self.last.insert(0, 24 + self.end[index] - self.begin[index])
                elif index == 3:
                    self.last.insert(0, 31 + self.end[index] - self.begin[index])
                elif index == 4:
                    self.last.insert(0, 12 + self.end[index] - self.begin[index])
                self.end[index + 1] -= 1

        for index in range(6):
            if self.last[index]:
                self.tmp.append(str(self.last[index]) + self.unit[index])
        self.prompt = '总共运行了' + ''.join(self.tmp)
        self.tmp = []
        self.begin = []
        self.end = []

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

