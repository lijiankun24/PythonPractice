#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


# 在输入字符串的时候，必须带有 "" 或 ''，否则将会出错
username = input('请输入用户名：')
password = input('请输入密码：')

if username == "admin" and password == "123":
    print "请进入"
else:
    print "请滚蛋"

"""
在 Python 中没有大括号 {}，使用缩进的方式来设置代码层次结构的；
在分支结构中，如果有多条语句需要执行，则使这几条语句具有相同的缩进
"""
year = int(input("请输入年份："))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if is_leap:
    print "闰年"
    print '瑞雪兆丰年'
else:
    print "平年"
    print '平平淡淡才是真'

"""
请输入三角形的边长，会自动计算其周长和面积
"""
a = float(input('请输入 a = '))
b = float(input('请输入 b = '))
c = float(input('请输入 c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长是 %f ' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积是 %f ' % area)
else:
    print '不是三角形'

