# -*- coding: utf8 -#-
import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, x, y):
        dx = x - self.x
        dy = y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)


if __name__ == '__main__':
    point = Point(10, 10)
    print point
    point.move_by(10, 10)
    print point
    print point.distance(10, 10)
