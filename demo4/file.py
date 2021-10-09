# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/16 9:02
# @File : file.py

'''
f = open("test.txt","w")   #打开文件，打开模式 w （写）

f. write("Hello world,I am here!")  #将字符串写入文件中
f.close() #关闭文件
'''

'''
#read 方法，读取指定的字符，开始时定位在文件头部，每执行一次向后移动指定字符数
f = open("test.txt","r") 

content = f.read(5)

print(content)

content = f.read(5)

print(content)
f.close()
'''

'''
f = open("test.txt","r")

content=f.readlines() #一次性读取全部文件为列表，每一行是一个字符串元素

i=1
for temp in content:
    print("%d:%s"%(i,temp))
    i+=1

print(content)

f.close()
'''

f=open("test.txt","r")

content=f.readline()
print("1:%s"%content)

content=f.readline()
print("2:%s"%content)

f.close()



