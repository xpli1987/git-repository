#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-06-27
'''
定制一个列表，同样要求记录列表中每个元素被访问的次数。这一次我们希望定制的列表功能更加全面一些，
比如支持 append()、pop()、extend() 原生列表所拥有的方法。你应该如何修改呢？
要求1：实现获取、设置和删除一个元素的行为（删除一个元素的时候对应的计数器也会被删除）
要求2：增加 counter(index) 方法，返回 index 参数所指定的元素记录的访问次数
要求3：实现 append()、pop()、remove()、insert()、clear() 和 reverse() 方法（重写这些方法的时候注
意考虑计数器的对应改变）
'''
class Mylist:
    def __init__(self,*args):   #列表有多个元素，所以这里使用非关键字收集参数

        self.value = [x for x in args]   #使用列表推导式把传入的元素放到value列表中

        #定义一个counter来根据value列表的索引记录元素被访问的次数
        self.c_dict = {}.fromkeys(range(len(args)),0)

        self.tmp = dict()

    def __len__(self):   #定义获取容器容量方法
        return len(self.value)

    def __getitem__(self, key):
        if key <= len(self.value)-1:
            self.c_dict[key] += 1
            return self.value[key]
        else:
            print('值不存在')

    def __repr__(self):
        return self.value

    def __setitem__(self, key, value):
        self.value[key] = value

    def __delitem__(self, key):
        del self.c_dict[key]
        del self.value[key]

    def counter(self,key):
        return self.c_dict[key]

    def append(self,value):
        self.value.append(value)
        self.c_dict[len(self.c_dict)] = 0

    def pop(self):
        self.value.pop()
        del self.c_dict[len(self.c_dict)-1]

    def remove(self,value):
        self.index = self.value.index(value)
        self.value.remove(value)
        del self.c_dict[self.index]
        for each_key in self.c_dict.keys():
            if each_key > self.index:
                self.tmp[each_key-1] = self.c_dict[each_key]
            else:
                self.tmp[each_key] = self.c_dict[each_key]
        self.c_dict = self.tmp
        self.tmp = dict()

    def insert(self,index,value):
        self.value[index] = value
        for each_key in self.c_dict.keys():
            if each_key >= index:
                self.tmp[each_key + 1] = self.c_dict[each_key]
            else:
                self.tmp[each_key] = self.c_dict[each_key]
        self.tmp[index] = 0
        self.c_dict = self.tmp
        self.tmp = dict()

    def clear(self):
        self.value.clear()
        self.c_dict = dict()

    def reverse(self):
        self.value.reverse()
        for each_key in self.c_dict.keys():
            self.tmp[len(self.value)-1-each_key] = self.c_dict[each_key]
        self.c_dict = self.tmp
        self.tmp = dict()