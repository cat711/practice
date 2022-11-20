#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#! usr/bin/env python3
# -*- coding: utf-8 -*-
# age = int(input("please enter your age"))
# if age >= 18:
#     print("adult")
# else:
#     print("teenager")
s4 = r'''Hello,
Bob!'''
print(s4)
ord('A')
ord('中')
chr(66)
chr(25991)
'ABC'.encode('ascii')
'中文'.encode('utf-8')
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
len('ABC')
print('Hello,%s' % 'world')
print('Hi,%s,you have $%d to pay.' % ('Bob', 10000))
print('Hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125))
r = 2.5
s = 3.14 * r ** 2
print(f'The area if a cricle with radius {r} is {s:.2f}')
s1 = 72
s2 = 85
print("s1 + s2 = ",s1+s2)
print('S1的值为：%d,s2的值为：%d' % (s1,s2))
print('s1的值为{0},s2的值为{1}'.format(s1,s1))
print(f's1的值为{s1},s2的值为{s2}')
classmates = ['张三','李四','王五']
print(classmates)
print(len(classmates))
print(classmates[2])
classmates[1] = "赵六"
# classmates[3] = "孙七"
print(classmates[-1])
classmates.append("Adam")
classmates.insert(2,'Bob')
classmates.pop()
classmates.pop(3)
names = ('Michael','Bob','Tracy')
L = [
    ['张三','李四','王五'],
    ['Apple','orange','banana'],
    ['X','Y','Z']
]
print(L[2:])
L.append(['A','B','C'])
L.pop(0)
L.insert(1,['Adam','Bob'])
print(len(L))
print(L)
age = 20
# if age >= 18:
#     print('your age is,'age)
#     print('adult')
# else:
#     print('your age is',age)
#     print('teenager')
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
birth = int(input('please enter your birsh:'))
if birth <= 2000:
    print('00前')
else:
    print('00后')
height = float(input('please enter your height:'))
weight = float(input('please enter your weight:'))
bmi = weight / (height * height)
print(f'BMI = {bmi:.2f}')
if bmi > 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')
score = str(input('please enter your score:'))
match score:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('及格')
    case _:
        print('不及格')
age = 15
match age:
    case x if x <10:
        print(f'<10 years old: {x}')
    case 10:
        print('10 years old')
    case 19:
        print('19 years old')
    case _:
        print(f'>19 years old: {age}')
args = ['gcc','hello.c','world.c']
#args = ['clean']
#arge = ['gcc']
match args:
    case ['gcc']:
        print('gcc:missing source file(s)')
    case ['gcc', file1, *files]:
        print('gcc compile:' + file1 + ',' + ','.join(files))
    case ['clean']:
        print('clean')
    case _:
        print('unknown command')
names = ['Michael','Bob','Tracy']
for name in names:
    print(name)
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)
for x in range (0,101):
    sum = sum + x
print(sum)
sum = 0
n = 99
while n>0:
    sum = sum +n
    n = n-2
print(sum)
d = {'张三':95,'李四':75,'王五':80}
print(d['张三'])
d['赵六'] = 60
print('Bob' in d)
d.get('Bob', -1)
s = {1,2,3}
s0 = {4,5,6,2}
s.add(4)
s.remove(1)
s1 = s & s0
s2 = s | s0

