#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
判断是否为回文的函数：
1、使用递归方法
2、迭代方法
3、利用列表的reversed()方法
'''
#
# #方法一：递归方法
# def isplalindrome(string,end,start=0):
#     if start > end:
#         return 1
#     else:
#         return isplalindrome(string,start+1,end-1) if string[start] == string[end] else 0

# string = '上海自来水来自海上'
# end = len(string)-1
# if isplalindrome(string,end):
#     print('这是一个回文！')
# else:
#     print('这不是回文结构！')

#方法二：迭代方法
# def isplalindrome(string):
#     length = len(string)
#     print(length)
#     for i in range(length):
#         if i > length-i-1:
#             return 1
#         else:
#             if string[i] == string[length-i-1]:
#                 print(string[i],i)
#                 continue
#             else:
#                 print(string[i])
#                 return 0

#方法三：使用列表的reversed()方法
def isplalindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return 1
    else:
        return 0

string = '上海自来水来自海上'
if isplalindrome(string):
    print('这是一个回文！')
else:
    print('这不是回文！')