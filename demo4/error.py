# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/16 9:36
# @File : error.py

'''
print("------test1-----")
    f = open("123.txt","r")  #用只读模式打开了一个不存在的文件，报错
    print("------test2-----")  #发生异常
'''


'''
#捕获异常
try:
    print("------test1-----")
    f = open("123.txt","r")
    print("------test2-----")
except IOError:  #文件没找到属于 IO 异常（输入输出异常）
    pass #占位   #捕获异常执行的代码

'''

'''
try:
    print(num)
except NameError:   #异常类型想要被捕获，需要一致
    print("产生错误了")
'''

'''
#获取错误描述
try:
    print("------test1-----")
    f = open("123.txt","r")
    print("------test2-----")

    print(num)

#except(NameError,IOError) as result:  #将可能产生的所有异常类型，都放到下面的小括号中
except Exception as result: #Exception 可以承接任何异常
    print("产生错误了")
    print(result)
'''


#try  finally  和嵌套

import time
try:
    f = open("123.txt","r")

    try:   #判断文件打不打得开，打得开就停顿两秒进行finally，打不开就报异常；但是最后都会关闭文件
        while True:
            content = f.readline()
            if len(content) ==0:  #文件里没内容
                break
            time.sleep(2)   #休眠一下
            print(content)  #打印文件内容
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常")













