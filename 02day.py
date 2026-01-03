# #!usr/bin/env python3
# # -*- coding: utf-8 -*-
# abs(100)
# abs(-5)
# max(2,3,1,-5)
# int('123')
# int(12.34)
# float('1.23')
# float(1)
# str(1.23)
# str(100)
# bool(1)
# bool('')
# # res = hex(int(input('please enter a number:')))
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-99))
# # from abstest import my_abs
# # my_abs(9)
# def abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# import math
# def move(x,y,step,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x, y = move(100,100,60,math.pi/6)
# print(x,y)
#! usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
import cmath
# from tkinter.scrolledtext import example


def quadratic(a,b,c):
    if not all(isinstance(arg,(int,float)) for arg in [a,b,c]):
        raise TypeError('bad operand type')
    if a == 0:
        raise ValueError('a cannot be zero')
    delta = b * b - 4 * a * c
    if delta >= 0:
        x1 = (-b + sqrt(delta))/(2 * a)
        x2 = (-b - sqrt(delta))/(2 * a)
        return x1, x2
    else:
        x1 = (-1 * b + cmath.sqrt(delta))/(2 * a)
        x2 = (-1 * b - cmath.sqrt(delta))/(2 * a)
        return x1, x2


def test():
    examples = [(1,-3,2),(1,-2,1),(1,0,-4),(1,1,1),(0,2,-4),(0,0,5)]
    for a,b,c in examples:
        try:
            x1, x2 = quadratic(a,b,c)
            print(f'a={a},b={b},c={c},x1={x1},x2={x2}')
        except (TypeError,ValueError) as e:
            print(f'a={a},b={b},c={c},error={e}')

test()

