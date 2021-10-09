# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/26 16:33
# @File : poem.py

import time
f = open("gushi.txt","w",encoding='utf-8')
f.write("白日依山尽\n黄河入海流\n欲穷千里目\n更上一层楼")
f.close()

def readpoem():
    f = open("gushi.txt","r",encoding='utf-8')
    a = f.read(1024)
    print(a)
    print("打开文件成功！")
readpoem()
f.close()

def copypoem():
    try: #打开旧文件
        b = open("gushi.txt", "r", encoding='utf-8')

        #按照新的名字 打开文件
        new_file = open("copy.txt", 'w', encoding='utf-8')
        try:
            while True:
                #读取要复制的文件里的内容
                content = b.read(1024)
                if len(content) == 0:  # 文件里没内容
                    break
                time.sleep(0.5)  # 休眠一下
                print("开始复制文件！")
                # 把之前复制的内容写到新的文件里
                new_file.write(content)
                print("复制完毕！")
        finally:
            f.close()
            new_file.close()

    except Exception as result:
        print("发生异常")

copypoem()