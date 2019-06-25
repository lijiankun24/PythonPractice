# -*- coding: utf8 -*-


def test1():
    # 定义一个 list
    list1 = [1, 5, 2, 3, 9]
    print list1                 # [1, 3, 5, 7, 9]
    # 定义一个 list
    list2 = ['hello'] * 5
    print list2                 # ['hello', 'hello', 'hello', 'hello', 'hello']
    # 打印 list 的数据类型
    print type(list1)           # <type 'list'>
    print type(list2)           # <type 'list'>
    # 获取 list 的长度
    print len(list1)            # 5
    # 获取 list 中的最大值
    print max(list1)            # 9
    # 获取 list 中的最小值
    print min(list1)            # 1
    # 将 list 升序排序
    print sorted(list1)         # [1, 2, 3, 5, 9]


def test2():
    list_one = [1, 5, 2, 3, 5, 9]
    # 取指定 index 位置的值
    print list_one[1]                # 5
    # 查找 value = 5 首次出现的位置
    print list_one.index(5)          # 1
    # 查找 value = 5 在指定的 [start, end) 范围内首次出现的位置
    print list_one.index(5, 2, 5)    # 4
    # print list_one.index(10, 2, 5)   # 如果不存在会抛出异常 ValueError: 10 is not in list
    # 查找 value = 5 在 list 中出现的次数
    print list_one.count(5)          # 2


def test3():
    list_one = [1, 5, 2, 3, 5, 9]
    # 向 list 中的指定位置插入值
    list_one.insert(0, 99)
    print list_one                   # [99, 1, 5, 2, 3, 5, 9]
    # 可以插入不同类型的数据，也不会报错
    list_one.insert(2, '100')        # [99, 1, '100', 5, 2, 3, 5, 9]
    print list_one
    # 修改指定索引位置的数据
    list_one[4] = 100
    print list_one                   # [99, 1, '100', 5, 100, 3, 5, 9]
    # 在 list 末尾添加元素
    list_one.append(200)
    print list_one                   # [99, 1, '100', 5, 100, 3, 5, 9, 200]
    # 在 list 末尾拼接 list
    list_one.extend([300, 400, 500, 600])
    print list_one                   # [99, 1, '100', 5, 100, 3, 5, 9, 200, 300, 400, 500, 600]


def test4():
    list_one = [1, 5, 2, 3, 5, 9]
    print list_one                   # [1, 5, 2, 3, 5, 9]
    # 删除 value = 5 第一次出现的值
    list_one.remove(5)
    print list_one                   # [1, 2, 3, 5, 9]
    # 删除末尾的值
    list_one.pop()
    print list_one                   # [1, 2, 3, 5]
    # 删除 index = 3 位置的值
    list_one.pop(3)
    print list_one                   # [1, 2, 3]


def test5():
    list_one = [1, 5, 2, 3, 5, 9]
    print list_one                   # [1, 5, 2, 3, 5, 9]
    # 按升序排序
    list_one.sort()
    print list_one                   # [1, 2, 3, 5, 5, 9]
    # 按降序排序
    list_one.sort(reverse=True)
    print list_one                   # [9, 5, 5, 3, 2, 1]
    list_one.append(999999)
    print list_one                   # [9, 5, 5, 3, 2, 1, 999999]
    # 反转字符串
    list_one.reverse()
    print list_one                   # [999999, 1, 2, 3, 5, 5, 9]


def test6():
    list_one = ['hello1', 'hello2', 'hello3', 'hello4', 'hello5']
    # 遍历 list
    for item in list_one:
        print item
    # 遍历 list 得到 index & value
    for index, item in enumerate(list_one):
        print('%d is %s ' % (index + 1, item))
    for item in enumerate(list_one):
        print item                   # (0, 'hello1') (1, 'hello2') (2, 'hello3') (3, 'hello4') (4, 'hello5')


def test7():
    """
    列表[开始索引:结束索引:步长] = [start, end, step]，不包括结束索引
        如果 step 为正数，start 和 end 的默认值分别是 0 和 length
        如果 step 为负数，start 和 end 的默认值分别是 -1 和 -(length + 1)
    start 和 end 可以为正数或者负数
        如果为正数，则按照 0,1,2,3,4 …… length
        如果为负数，则按照 -(length+1), -(length), -(length-1),-(length-2) …… -1
    """
    list_one = [1, 5, 2, 3, 5, 9]
    # 截取完整的 list，start 和 end 的默认值是 0 和 length
    print list_one[:]                       # [1, 5, 2, 3, 5, 9]
    # 截取 [0, 3) 的元素
    print list_one[:3]                      # [1, 5, 2]
    # 截取 [3, length] 的元素
    print list_one[3:]                      # [3, 5, 9]
    # 截取 [0, length] 的元素，step 步长为 2
    print list_one[::2]                     # [1, 2, 5]
    # 截取 [0, length] 的元素，step = -1 表示从尾向前
    print list_one[::-1]                    # [9, 5, 3, 2, 5, 1]
    # start= -1 表示最后一个元素，end = 3 表示第3个元素
    print list_one[-1:3:-1]                 # [9, 5]
    # start=-1 表示最后一个元素，如果 step = -1, end 默认第一个元素的位置
    print list_one[2::-1]                   # [2, 5, 1]


if __name__ == '__main__':
    test7()
