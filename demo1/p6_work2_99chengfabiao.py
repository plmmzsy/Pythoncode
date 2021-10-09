# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/8/19 15:59
# @File : p6_work2_99chengfabiao.py

#用for循环和while循环实现九九乘法表

我自己写的
c = 0
for a in range(0,9):
    a+=1
    for b in range(1,10):
        c = a*b
        if b>a:
            print("\t")
            continue
        else:
            print("%d * %d = %d  " % (a, b, c),end="")
            b += 1


for x in range(1,10):
    print("\t")
    for y in range(1,x+1):
        result=x*y
        print("%d*%d=%d"%(x,y,x*y),end="\t")