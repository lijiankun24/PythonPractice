# -*- utf8 -*-


class Student(object):

    __slots__ = ('_name', '_age', '_school')

    def __init__(self, name, age):
        self._name = name
        self._age = age

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


if __name__ == '__main__':
    student = Student('lijiankun24', 24)
    student.introduce_self()
    student.age = 10
    student.introduce_self()
    print student.age
    print student.name
    student._name = 'wwwwww'
    student._school = 'school'
    print student._name
    print student._school
    # student._hhh = 'hhh'                  #
    # student.name = 'hhhh'
