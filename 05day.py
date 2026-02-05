#!usr/bin/env python3
# -*- coding:utf-8 -*-
def inc():
    x = 0
    def fn():
        nonlocal x
        x = x +1
        return x
    return fn
f = inc()
print(f())
print(f())
print(list(map(lambda x:x*x,[1,2,3,4,5])))
def build(x,y):
    return lambda: x*x+y*y
print(list(filter(lambda x:x%2==1,range(1,20))))
def now():
    print('2026-1-16')
f = now
print(now.__name__)
print(f.__name__)
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2026-1-16')

# 自定义log文本
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():'% (text,func.__name__))
            return func(*args,**kw)
        return wrapper()
    return decorator()
@log('execute')
def now():
    print('2026-1-16')
now = log('execute')(now)
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
import _functools
int2 = functools.partial(int,base=2)
' a test moudle'
__author__ = 'Administrator'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) ==2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')
if __name__ == '__main__':
    test()
def _private_1(name):
    return 'Hello,%s!' % name
def _private_2(name):
    return 'Hi,%s!' % name
def greeting(name):
    if len(name) >3:
        return _private_1(name)
    else:
        return _private_2(name)
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
bart = Student()
bart.name = 'Bart Simpson'
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    pass
print(dir('ABC'))
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
hasattr(obj,'x')
hasattr(obj,'y')
setattr(obj,'y',19)
hasattr(obj,'y')
getattr(obj,'y',404)
class Student():
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count = Student.count + 1
s = Student('Bob')
s.score =  90




