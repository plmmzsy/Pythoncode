# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/8/18 15:49
# @File : hello.py

#这是我的第一个python程序
print("hello", end="")
print("Hello world!")

'''
这是第一行注释
这是第二行注释

'''

print("python")

print("标准化输出字符串")

a=10

print("这是变量",a)


age=18

print("我的年纪是：%d 岁"%age)
#占位符%d(有符号的十进制整数)
# %s 通过str()字符串转换来格式化

print("我的名字是%s，我的国籍是%s"%("小周","中国"))


print("www","baidu","com",sep=".") #sep表示分割

print("hello",end="") #表示不换行
print("hello",end="\t") #相当于tab键
print("world",end="\n") #换行
