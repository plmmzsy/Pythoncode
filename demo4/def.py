# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/15 14:56
# @File : def.py


#函数的定义
'''
def printinfo():
    print("----------------------")
    print("  人生苦短，我用python  ")
    print("----------------------")


#函数的调用

printinfo()
'''


#带参的函数
'''
def add2Num(a,b):
    c = a+b
    print(c)

add2Num(11,22)
'''

#带返回值的函数
'''
def add2Num(a,b):
    return a+b #通过 return来返回运算结果

result = add2Num(11,22)
print(result)
#print(add2Num(11,22))
'''

#返回多个值的函数
'''
def divide(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu  #多个返回值用逗号分隔

sh,yu = divide(5,2)  #需要使用多个值来保存返回内容
print("商：%d，余数：%d"%(sh,yu))
'''


'''
#打印一条线
def hengxian(n):
    a= print("-"*n)

#调用上面的函数打印任意长度的线
def shuru():
    c = int(input("请输入想打印的横线的长度："))
    hengxian(c)

shuru()
'''

'''
#求三个数的和
def sum(a,b,c):
    return a+b+c

print(sum(10,20,30))

#求三个数的平均值
def avg(a,b,c):
    sumresult=sum(a,b,c)
    avg=sumresult//3
    return avg

result = avg(10,20,30)
print("平均值为：%d"%result)
'''


#全局变量和局部变量
'''
def test1():
    a = 300  #局部变量
    print("test1-------修改前： a = %d"%a)
    a = 100
    print("test1-------修改前： a = %d"%a)

def test2():
    a = 500  #不同的函数可以定义相同的名字，彼此无关
    print("test2------a= %d"%a)

test1()
test2()
'''


'''
a= 100  #全局变量
def test1():
    print(a)

def test2():
    print(a)  #调用全局变量a

test1()
test2()
'''


#全局变量和局部变量相同名字：局部变量优先使用；没有局部变量，默认访问全局变量


#在函数中修改全局变量
a = 100
def test1():
    global a #声明全局变量在函数中的标识符 global
    print("test1-------修改前： a = %d"%a)
    a = 200
    print("test1-------修改前： a = %d"%a)

def test2():
    print("test2------a= %d"%a)  #全局变量已经被修改

test1()
test2()