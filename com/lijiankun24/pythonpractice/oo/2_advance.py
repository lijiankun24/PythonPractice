# -*- coding: utf8 -*-

from math import sqrt
import random


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def watch_movie(self):
        if self._age >= 18:
            print '%s is watching 泰坦尼克号' % self._name
        else:
            print '%s is watching 熊出没' % self._name


class Student(Person):
    __slots__ = ('_name', '_age', '_school', '_title')

    def __init__(self, name, age):
        super(Student, self).__init__(name, age)

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, age):
        self._age = age

    def introduce_self(self):
        print('My name is %s and I\'am %d years old.' % (self._name, self._age))


class Teacher(Person):
    def __init__(self, name, age, title='default'):
        super(Teacher, self).__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self):
        print('%s is teaching course ' % self._title)


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self.a) * (half - self.b) * (half - self.c))

    @classmethod
    def instance_triangle(cls):
        x = random.randint
        y = random.randint
        z = random.randint
        return cls(x, y, z)

    @staticmethod
    def is_valid(a, b, c):
        return (a + b) > c and (b + c) > a and (a + c) > b


if __name__ == '__main__':
    student = Student('lijiankun24', 20, 'hhhhh')
    print student.name
    print student.age
    student.watch_movie()

    teacher = Teacher('lijiankun24', 30)
    teacher.teach()
    teacher.title = '高级教师'
    teacher.teach()

    # triangle_one = Triangle.instance_triangle()
    # print triangle_one
    #
    # x = 3
    # y = 4
    # z = 5
    # if Triangle.is_valid(x, y, z):
    #     triangle = Triangle(x, y, z)
    #     peri = triangle.perimeter()
    #     area = triangle.area()
    #     print peri
    #     print area
    # else:
    #     print '无法构成三角形'

