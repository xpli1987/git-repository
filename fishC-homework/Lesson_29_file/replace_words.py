#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
文件内容进行替换：
1、用户输入待替换的文件名
2、需要被替换的字符串
3、替换的字符串
4、统计将被替换数量并询问是否进行替换
    1）输入yes进行替换
    2）输入no不进行替换
'''

def count_words(filename,old_words,new_words):
    with open(filename,'r') as f:
        #进行统计被替换字符数量和进行替换操作
        old_str = f.read()
        words_count = old_str.count(old_words)
        new_str = old_str.replace(old_words,new_words)
    return words_count, new_str

def write_file(filename,doc_str):
    #进行写入操作
    with open(filename,'w') as f:
        f.write(doc_str)
    print('替换完成！！！')

def main():
    file_name = input('请输入文件名：')
    old_words = input('请输入需要被替换的单词或字符：')
    new_words = input('请输入新的单词或字符：')
    count_num, replace_doc = count_words(file_name,old_words,new_words)
    prompt = \
'''
文件%s中共有%d个【%s】
您确定要把所有的【%s】替换为【%s】吗？
【YES/NO】:
'''\
%(file_name,count_num,old_words,old_words,new_words)
    user_order = input(prompt)
    if user_order.upper() == 'YES':
        write_file(file_name,replace_doc)
    else:
        print('已放弃了保存！')

if __name__ == '__main__':
    main()
