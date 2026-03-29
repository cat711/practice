#!usr/bin/env python3
# -*- coding:utf-8 -*-
# from types import MethodType
# class Student(object):
#     __slots__ = ('name','age')
# s = Student()
# s.name = 'Michael'
# def set_age(self,age):
#     self.age = age
# s.set_age = MethodType(set_age,s)
# s.set_age(25)
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer!')
#         if value <0 or value > 100:
#             raise ValueError('score must between 0~100!')
#         self._score = value
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self,value):
#         self._birth = value
#     @property
#     def age(self):
#         return 2026 - self._birth
from distutils.command.install import value


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


# class Student(object):
#     def get_score(self):
#         return self._score
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer')
#         if value <0 or value > 100:
#             raise ValueError('score must between 0~100')
#         self._score = value
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value
class Screen(object):
    __slots__ = ('_width','_height')
    def __init__(self,width=0,height=0):
        self._width = width
        self._height = height
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @width.setter
    def width(self,value):
        if not isinstance(value,(int,float)) or value <0:
            raise ValueError('width must be int or float or value must be >0')
        self._width = value
    @height.setter
    def height(self,value):
        if not isinstance(value,(int,float)) or value <0:
            raise ValueError('height must be int or float or value must be >0')
        self._height = value
