# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/18 9:56
# @File : spider.py

'''
def main():
    print("Hello")

main()

if __name__=="__main__":
    main()
'''

from bs4 import BeautifulSoup #网页解析，获取数据
import re  #正则表达式，进行文字匹配
import urllib.request,urllib.error  #指定URL，获取网页数据
import xlwt  #进行 excel 操作
import sqlite3 #进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    #2.逐一解析数据


#爬取网页
def getData(baseurl):
    datalist = []
    return datalist


#3.保存数据
def saveData(savepath):
    print("save...")
