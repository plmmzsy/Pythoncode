# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/6 18:11
# @File : demo1_String.py

'''
word = '字符串'
sentence = "这是一个句子"
paragraph = """
        这是一个段落
        可以由多行组成
"""

print(word)
print(sentence)
print(paragraph)
'''

'''
#单引号和双引号的区别(第一种情况可以正常输出，第二种无法正常输出，但是可以通过转义字符输出3）

my_str = "I'm a student"
print(my_str)

#my_str = 'I'm a student'


my_str = 'I\'m a student'
print(my_str)



#当字符串中有双引号
my_str = "Jason siad \" I like you \""
my_str = 'Jason siad \" I like you \"'
print(my_str)

#字符串截取，函数
str = 'kunming'
print(str)
print(str[0:6])#把字符串当做列表，截取部分[起始位置:结束位置:步进值]
print(str[1:7:2])

print(str[5:])
print(str[:5])#不包含第五个，但是从第五个开始的时候包含第五个

#连接，重复打印
print(str+",hello")
print(str*3)
'''

print("hello\nchengdu") #使用反斜杠实现转义字符功能
print(r"hello\nchengdu") #让转义字符失效，显示原始字符串，直接输出





