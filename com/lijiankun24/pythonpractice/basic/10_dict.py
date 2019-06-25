# -*- coding: utf8 -*-


def test1_dict():
    # dict 中，要求 key 是不可变的元素（元组也可以），value 可以是任意类型的数据
    dict_one = {'key1': 'value1', 1: 10, 'Boy': True, False: 'Girl', (1, 100): 100, 'list': [1, 2, 3, 4]}
    print dict_one
    print type(dict_one)
    print len(dict_one)


def test2_dict():
    dict_one = {'key1': 'value1', 'key2': 'value2', 'Boy': True, False: 'Girl'}
    print dict_one                          # {False: 'Girl', 'key2': 'value2', 'key1': 'value1', 'Boy': True}

    # dict[key] = value，若 key 存在则更新 value，若不存在则添加 key:value
    dict_one['key1'] = 100
    dict_one['key3'] = 100
    print dict_one                          # {False: 'Girl', 'key2': 'value2', 'key1': 100, 'key3': 100, 'Boy': True}

    # dict[key] 若不存在，则直接抛出异常 KeyError: 'left'
    # print dict_one['key4']                  # KeyError: 'left'
    # dict.get(key, defaultValue) get方法也是通过键获取对应的值，但是可以设置默认值
    print dict_one.get('key4', '10000')     # 10000

    # 异常第一个元素
    print dict_one.popitem()                # (False, 'Girl')
    # 移除对应 key 的元素
    print dict_one.pop('key1')              # 100
    print dict_one                          # {'key2': 'value2', 'key3': 100, 'Boy': True}

    # 合并字典，如果有相同的 key，则使用新的 value 值
    print dict_one.update({'Boy': False, 'key4': 'value4'})
    print dict_one                          # {'Boy': False, 'key3': 100, 'key2': 'value2', 'key4': 'value4'}

    # 清空字典
    dict_one.clear()
    print dict_one                          # {}


def test3_dict():
    dict_one = {'key1': 'value1', 'key2': 'value2', 'Boy': True, False: 'Girl'}
    # 直接遍历 dict_one 得到的是每一个 key
    for key in dict_one:
        print key
    # 遍历 dict_one.items() 得到的是每一个 (key, value)
    for item in dict_one.items():
        print item
    # 遍历 dict_one.keys() 得到的是每一个 key
    for key in dict_one.keys():
        print key
    # 遍历 dict_one.values() 得到的是每一个 value
    for value in dict_one.values():
        print value

    # dice.keys() 和 dict.values() 得到的是 list 类型的 key 和 value
    print dict_one.values()                 # ['Girl', 'value2', 'value1', True]
    print dict_one.keys()                   # [False, 'key2', 'key1', 'Boy']


if __name__ == '__main__':
    test3_dict()
