#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
判断输入的字符串是否为回文字符串:
判断方法：
比较字符串第start个和最后end个是否相同，如果相同则比较第start+1个与end-1个是否相同，依此类推
最终如果start > end则表示为回文字符串
如果比较不相同，则为非回文字符串
'''
def is_palintic_string(string,start,end):
    if start > end:
        return 1
    else:
        return is_palintic_string(string,start+1,end-1) if string[start] == string[end] else 0

string = input('请输入字符串，判断是否为回文字符串：')
length = len(string)
if is_palintic_string(string,0,length-1):
    print('这是一个回文字符串！')
else:
    print('这不是回文字符串。。。')