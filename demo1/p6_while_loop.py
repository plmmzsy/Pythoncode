# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/8/19 15:10
# @File : p6_while_loop.py

'''
i = 0
while i< 5 :
    print("当前是第%d次执行循环" %(i+1))
    print("i=%d" %i)
    i+=1
'''

#1-100求和
#我自己写的
i=0
a = 0
while i<100 :
    i += 1
    a += i

print(a)

n = 100
sum = 0
counter = 1
while counter <=n:
    sum=sum+counter
    counter+=1

print("1- %d 和为：%d"%(n,sum))

count=0
while count<5:
    print(count,"<5")
    count+=1
else:
    print(count,"大于或等于5")

i=0
while i<10:
    i=i+1
    print("-"*30)
    if i==5:
        break
    print(i)

i=0
while i<10:
    i=i+1
    print("-"*30)
    if i==5:
        continue #跳过了第五次循环
    print(i)

