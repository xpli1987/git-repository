#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss__XPLI
'''
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
'''
import time,functools

def metric(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print(wrapper.__name__)
        start = time.perf_counter()
        func(*args,**kw)
        end = time.perf_counter()
        print('%s executed in %s ms' %(func.__name__,end-start))
        return func(*args,**kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)   #相当于fast(11,22)=metric(fast)(11,22)=wrapper(11,22)

s = slow(11, 22, 33)  #相当于slow(11,22,33)=metric(slow)(11,22,33)=wrapper(11,22,33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')