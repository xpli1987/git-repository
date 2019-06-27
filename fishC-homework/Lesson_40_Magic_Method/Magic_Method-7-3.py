#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-23
'''
在Magic_Method-7-2.py基础上不再使用time.localtime方法（因为localtime方法默认一个月有31天）。
改为使用time.perf_counter()或者time.process_time()方法
同时增加一个 set_timer() 方法，用于设置默认计时器（默认是 perf_counter()，可以通过此方法修
改为 process_time()）
'''
import time

class MyTimer():
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.prompt = '未开始计时!'
        self.last = 0
        self.method = 'perf_counter'

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

