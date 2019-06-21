#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特性的数据结构。至少需要有以下方法：
方法名	含义
isEmpty()	判断当前栈是否为空（返回 True 或 False）
push()	往栈的顶部压入一个数据项
pop()	从栈顶弹出一个数据项（并在栈中删除）
top()	显示当前栈顶的一个数据项
bottom()	显示当前栈底的一个数据项
'''


class Stack():
    def __init__(self):
        self.str = []

    def isEmpty(self):
        return len(self.str) == 0

    def push(self,data):
        self.data = data
        self.str.append(self.data)

    def pop(self):
        self.str.pop()

    def top(self):
        return self.str[-1]

    def bottom(self):
        return self.str[0]
