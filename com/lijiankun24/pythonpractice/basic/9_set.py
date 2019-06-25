# -*- coding: utf8 -*-


def test1_set():
    set_one = {1, 5, 4, 3, 2, 7, 8, 5, 9}
    set_two = set(range(1, 10))
    print set_one
    print set_two
    print type(set_one)
    print type(set_two)
    print len(set_one)
    print min(set_one)
    print max(set_one)
    print sorted(set_one)
    print sorted(set_one, reverse=False)
    print 1 in set_two
    print 11 in set_one
    print 11 not in set_one


def test2_set():
    set_one = {1, 5, 4, 3, 2, 7, 8, 5, 9}
    print set_one                   # set([1, 2, 3, 4, 5, 7, 8, 9])
    # 向集合中添加元素
    set_one.add(10)
    print set_one                   # set([1, 2, 3, 4, 5, 7, 8, 9, 10])
    # 向集合中添加元素，
    set_one.add(7)
    print set_one                   # set([1, 2, 3, 4, 5, 7, 8, 9, 10])
    # 随机移除集合中的一个元素，若集合为空则抛出 KeyError
    set_one.pop()
    print set_one                   # set([2, 3, 4, 5, 7, 8, 9, 10])
    # 从集合中移除 value = 7 的元素
    set_one.remove(7)
    print set_one                   # set([2, 3, 4, 5, 8, 9, 10])
    # 若集合中没有这个元素，则会抛出异常 KeyError
    # set_one.remove(11)
    # print set_one                 # KeyError: 11
    # 从集合中移除 value == 11 的元素，若不存在也不会抛出异常
    set_one.discard(11)
    print set_one                   # set([2, 3, 4, 5, 8, 9, 10])
    # 从集合中移除 value == 4 的元素
    set_one.discard(4)
    print set_one                   # set([2, 3, 5, 8, 9, 10])
    # 取两个集合的并集，并赋值给左侧的集合
    set_one.update({10, 11, 12})
    print set_one                   # set([2, 3, 5, 8, 9, 10, 11, 12])
    # copy 一个集合至另一个集合
    set_two = set_one.copy()
    print set_two                   # set([2, 3, 5, 8, 9, 10, 11, 12])
    # 清空集合
    set_one.clear()
    print set_one                   # set([])
    print set_two                   # set([2, 3, 5, 8, 9, 10, 11, 12])


def test3_set():
    set_one = {1, 2, 3, 4}
    set_two = {4, 5, 6}
    # 交集
    print set_one & set_two                         # set([4])
    print set_one.intersection(set_two)             # set([4])
    # 并集
    print set_one | set_two                         # set([1, 2, 3, 4, 5, 6])
    print set_one.union(set_two)                    # set([1, 2, 3, 4, 5, 6])
    # 差集
    print set_one - set_two                         # set([1, 2, 3])
    print set_one.difference(set_two)               # set([1, 2, 3])
    # 对称差
    print set_one ^ set_two                         # set([1, 2, 3, 5, 6])
    print set_one.symmetric_difference(set_two)     # set([1, 2, 3, 5, 6])
    set_union = set_one & set_two
    print set_union                                 # set([4])
    # A.issubset(B) A 是否是 B 的子集
    print set_union.issubset(set_one)               # True
    print set_union.issubset(set_two)               # True
    # A.issuperset(B) A 是否是 B 的超集
    print set_one.issuperset(set_union)             # True
    print set_one.issuperset(set_two)               # False

    # 不论上面怎么操作，都不会改变 set 的原始值
    print set_one                                   # set([1, 2, 3, 4])
    print set_two                                   # set([4, 5, 6])
    # 求差集并赋值给左侧的集合
    set_one.difference_update(set_two)
    print set_one                                   # set([1, 2, 3])
    # 求交集并赋值给左侧的集合
    set_one = {1, 2, 3, 4}
    set_one.intersection_update(set_two)
    print set_one                                   # set([4])
    # 求对称差并赋值给左侧的集合
    set_one = {1, 2, 3, 4}
    set_one.symmetric_difference_update(set_two)
    print set_one                                   # set([1, 2, 3, 5, 6])

    set_one = {1, 2, 3, 4}
    set_two = {4, 5, 6}
    # A.isdisjoint(B) A 和 B 集合中是否不存在相同的元素
    #   False 表示两个集合中存在相同的元素
    #   True 表示两个集合中的元素完全不相同
    print set_one.isdisjoint(set_two)               # False
    set_two = {5, 6}
    print set_one.isdisjoint(set_two)               # True


if __name__ == '__main__':
    test1_set()
