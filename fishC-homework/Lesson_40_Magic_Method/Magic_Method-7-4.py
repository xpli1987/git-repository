#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-23
'''
在Magic_Method-7-3.py基础上增加一个统计一个函数运行若干次的时间。
要求一：函数调用的次数可以设置（默认是 1000000 次）
要求二：新增一个 timing() 方法，用于启动计时器
'''
import time

class MyTimer():
    def __init__(self,func,times = 1000000):
        self.begin = 0
        self.end = 0
        self.prompt = '未开始计时!'
        self.last = 0
        self.method = 'perf_counter'
        self.func = func
        self.times = times

    def timing(self):
        self.start()
        for i in range(self.times):
            self.func()
        self.stop()

    def set_timer(self,method='process_time'):
        self.method = method

    def start(self):
        print('计时开始...')
        if self.method == 'process_time':
            self.begin = time.process_time()
        elif self.method == 'perf_counter':
            self.begin = time.perf_counter()

    def stop(self):
        if self.begin:
            if self.method == 'process_time':
                self.end = time.process_time()
            elif self.method == 'perf_counter':
                self.end = time.perf_counter()
            print('计时结束...')
            self._calc()
        else:
            print('提示：请先调用start()开始计时！')

    def _calc(self):
        self.last = self.end - self.begin
        self.prompt = '总共运行了%2f秒'%self.last
        self.begin = []
        self.end = []

    def __repr__(self):
        return self.prompt

    def __str__(self):
        return self.prompt

    def __add__(self, other):
        self.prompt = '总共运行了%2f秒'%(self.last+other.last)
        return self.prompt

