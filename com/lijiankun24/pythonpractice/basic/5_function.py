# -*- coding: utf8 -*-
from random import randint
from math import sqrt


def test_func1_factorial(num):
    """
    求阶乘
    """
    value = 1
    for num in range(1, num + 1, 1):
        value *= num
    return value


def test_func2_foo(a=10, b=20):
    """
    具有默认值的参数
    """
    print a - b


def test_func3_add(*args):
    """
    在参数名前面的*表示args是一个可变参数
    即在调用add函数时可以传入0个或多个参数
    """
    total = 0
    for i in args:
        total += i
    return total


def test_func4_roll_dice(count=2):
    total = 0
    for _ in range(count):
        total += randint(1, 6)
    return total


def test_func5_gcd(x, y):
    """
    最大公约数
    """
    (x, y) = (x, y) if x > y else (y, x)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def test_func6_lcm(x, y):
    """
    最小公倍数
    """
    return x * y / test_func5_gcd(x, y)


def test_func7_is_palindrome(num):
    """
    判断一个数是不是回文数
    """
    total = 0
    temp = num
    while temp > 0:
        total = total * 10 + temp % 10
        temp = temp / 10
    return total == num


def test_func8_is_prime(num):
    """
    判断一个数是否是素数
    """
    result = True
    if num <= 3:
        result = num > 1
    else:
        temp = int(sqrt(num))
        for i in range(2, temp):
            if temp % i == 0:
                result = False
                break
    print('%d is prime %r' % (num, result))


if __name__ == '__main__':
    inputNum = int(input("请输入数字："))
    test_func8_is_prime(inputNum)
