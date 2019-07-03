# -*- coding: utf8 -*-

from abc import abstractmethod


class Animal(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Animal):

    def make_voice(self):
        print '汪汪汪'


class Cat(Animal):

    def make_voice(self):
        print '喵喵喵'


if __name__ == '__main__':
    dog = Dog('狗')
    dog.make_voice()

    cat = Dog('猫')
    cat.make_voice()
