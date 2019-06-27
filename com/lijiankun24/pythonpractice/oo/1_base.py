# -*- coding: utf8 -*-


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course):
        print('%s is studying %s' % (self.name, course))

    def watch_movie(self):
        if self.age > 18:
            print('%s is watching 活着' % self.name)
        else:
            print('%s is watching 奥特曼' % self.name)


if __name__ == '__main__':
    student_one = Student('lijiankun24', 24)
    student_one.study('物理')
    student_one.watch_movie()
