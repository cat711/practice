# ! usr/bin/env python3
# -*- coding: utf-8 -*-
from collections.abc import Iterator
from functools import  reduce
from string import digits

# isinstance(iter([1,2,3]),Iterator)
# isinstance(iter('abc'),Iterator)
# it = iter([1,2,3,4,5])
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration as e:
#         print('Generator return value:',e.value)
#         break
# # f = abs()
# def add(x,y,f):
#     return f(x) + f(y)
# print(add(-5,-6,abs))
# def f(x):
#     return x*x
# r = map(f,[1,2,3,4,5,6])
# print(list(r))
# L=[]
# for n in [1,2,3,4,5,6]:
#     L.append(f(n))
# print(L)
# print(list(map(str,[9,8,7,6,5,4])))
# def add(x,y):
#     return x+y
# reduce(add,[1,2,3,4,5])
# def fn(x,y):
#     return x*10+y
# reduce(fn,[1,2,3,4,5])
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# reduce(fn,map(char2num,'13579'))
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def fn(x,y):
        return 10*x+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
def is_old(n):
    return n%2==1
list(filter(is_old,[1,2,3,4,5,6,7,8,9]))
list(filter(lambda n:n%2==1,[1,2,3,4,5,6,7,8,9]))
def not_empty(s):
    return s and s.strip()
list(filter(not_empty,['A','','B',None,'C','  ']))
def _old_iter():
    n = 1
    while True:
        n +=2
        yield n
def _not_divisible(n):
    return lambda x:x%n >0
def primes():
    yield 2
    it = _old_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
for n in primes():
    if n <100:
        print(n)
    else:
        break
sorted([36,5,8,-7,2,88])
sorted([36,5,8,-7,2,88],key=abs)
sorted_list = sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse = True)
print(sorted_list)
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
def by_score(t):
    return t[1]
L1 = sorted(L,key=by_name)
L2 = sorted(L,key=by_score,reverse=True)
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax +n
    return ax
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax  =ax +n
        return ax
    return sum()
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs










