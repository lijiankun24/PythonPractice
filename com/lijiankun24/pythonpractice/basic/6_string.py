# -*- coding: utf8 -*-


def test1():
    # 字符串可以是单引号''  也可以是双引号""
    str1 = 'abc123456'
    str2 = "abc123456789"
    print str1
    print str2

    # 通过 len() 方法打印字符串长度
    print len(str1)                       # 9
    print len(str2)                       # 12

    # 可以通过 type() 方法输出字符串数据类型 <type 'str'>
    print type(str1)                      # <type 'str'>
    print type(str2)                      # <type 'str'>


def test2():
    str1 = 'abc12345611'
    str2 = "abc123456789"
    # 通过 find 方法查找指定字符串的位置并返回 index
    print str1.find('12')                 # 3
    print str2.find('35')                 # -1

    # 也可以通过 index 方法查找字符串，如果查找不到会抛出异常
    # print str1.index('12')              # 3
    # print str2.index('35')              # ValueError: substring not found

    print str1.startswith("a")            # True
    print str1.endswith("5")              # False
    print str1.isalpha()                  # False
    print str1.isdigit()                  # False
    print str1.isalnum()                  # True


def test3():
    str1 = 'abc12345611'
    str2 = 'Hello world!'
    # 转换成大写
    print str1.upper()                    # ABC123456
    # 转换成小写
    print str2.lower()                    # hello world!
    # 将字符串中的字母反转大小写
    print str2.swapcase()                 # hELLO WORLD!
    # 第一个字符大写
    print str1.capitalize()               # Abc12345611
    # 字符串中每个单词的第一个字母大写
    print str2.title()                    # Hello World!


def test4():
    str1 = 'abc12345611'
    length1 = len(str1)
    print str1.center(length1 + 6, '*')   # ***abc123456***
    print str1.ljust(length1 + 6, '*')    # abc12345611******
    print str1.rjust(length1 + 6, '*')    # ******abc12345611
    print str1.count('1')                 # 3
    print str1.replace('1', '3')          # abc32345633


def test5():
    # 字符串[开始索引: 结束索引: 步长]，不包含结束索引
    string = '0123456789'
    # 字符串中 index = 3 处的字符，从 0 开始
    print string[3]                         # 3
    # start 至 end 处的字符串，[start, end)
    print string[0:3]                       # 012
    # 输出完整的字符串
    print string[:]                         # 0123456789
    # 截取 3 - 结束 的字符串
    print string[3:]                        # 3456789
    # 截取 开始 - 5 的字符串，不包括 index = 5 的字符
    print string[:5]                        # 01234

    # start 至 end 处的字符串，[start, end), step 步长为 2
    print string[0:6:2]                     # 024
    # 从开始至结尾，step 为 2
    print string[::2]                      # 02468
    # step 间距可以为负数，则从末尾开始计算
    print string[:5:-1]                     # 9876
    print string[:0:-2]                     # 97531
    # start 和 end 可以为负数，从末尾开始计算 index，-1、-2、-3、-4
    print string[-3:-1]                     # 78
    # 倒序一个字符串
    print string[::-1]                      # 9876543210


def test6():
    name = input("请输入姓名: ")
    age = int(input("请输入年龄: "))
    weight = float(input("请输入体重: "))
    print('name is %s, age is %d, weight is %.2f' % (name, age, weight))
    temp = (name, age, weight)
    print('name is %s, age is %d, weight is %.3f' % temp)


if __name__ == '__main__':
    test6()
