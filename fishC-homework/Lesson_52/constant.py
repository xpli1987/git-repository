#!/usr/bin/env pyhton
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-07-01
'''
在 const 模块中我们到底做了什么，使得这个模块这么有“魔力”呢？大家跟着小甲鱼的提示，
一步步来做你就懂了：
    提示一：我们需要一个 Const 类
    提示二：重写 Const 类的某一个魔法方法，指定当实例对象的属性被修改时的行为
    提示三：检查该属性是否已存在
    提示四：检查该属性的名字是否为大写
    提示五：我们这个 const 模块导入之后就把它当对象来使用
    （const.NAME = "FishC"）了呢？难道模块也可以是一个对象？没错啦，在 Python 中无处
    不对象，到处都是你的对象。使用以下方法可以将你的模块与类 A 的对象挂钩。
'''

class Const:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError('常量无法改变!')
        if not name.isupper():
            raise TypeError('常量必须为大写')
        #else:
        self.__dict__[name] = value

import sys
sys.modules[__name__] = Const()
#sys.modules函数是一个字典，包含了Python从运行开始导入的所有模块。
#sys.modules的键为模块名，值为模块对象
#把模块对象化，实际就是通过sys.modules()函数把导入的模块名对应的值修改为模块中的类
#从而实现模块实例化。
