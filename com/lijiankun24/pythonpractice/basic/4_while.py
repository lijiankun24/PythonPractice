# -*- coding: utf8 -*-
import random
import math


print '================BEGIN============================='
"""
判断一个数是否是素数
"""
number = int(input("请输入数字："))
if number <= 3:
    isPrime = number > 1
    print('%d是素数: %r' % (number, isPrime))
else:
    middle = int(math.sqrt(number))
    isPrime = True
    for temp in range(2, middle + 1):
        if number % temp == 0:
            isPrime = False
            break
    print '%d是素数: %r' % (number, isPrime)
print '================END============================='


print '================BEGIN============================='
"""
求100以内所有偶数的和
"""
sum = 0
for num in range(1, 101, 1):
    if num % 2 == 0:
        print num
        sum += num
print sum
print '================END============================='


print '================BEGIN============================='
"""
猜数字游戏
"""
target = random.randint(0, 10)
inputNum = int(input("请输入猜测的数字："))
while not target == inputNum:
    if inputNum > target:
        print '猜大了'
    elif inputNum < target:
        print '猜小了'
    else:
        print '游戏完成'
    inputNum = int(input("请输入猜测的数字："))
print '游戏完成'
print '================END============================='
