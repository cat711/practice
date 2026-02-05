# ! usr/bin/env python3
# -*- coding: utf-8 -*-
# def person(name,age,*,city,job):
#     print('name:',name,'age:',age,'city:',city,'job:',job)
# person('jack',24,city='Beijing',job='Engineer')
# def fact(n):
#     return fact_item(n,1)
# def fact_item(num,product):
#     if num == 1:
#         return product
#     return fact_item(num-1,num*product)
# def move(n,a,b,c):
#     if n ==1:
#         print(a,'-->',c)
#     else:
#         move(n-1,a,c,b)
#         print(a,'-->',c)
#         move(n-1,b,a,c)
# l = [i for i in range(1,100,2)]
# print(l)
# def trim(s):
#     if not s:
#         return s
#     start = 0
#     end = len(s)
#     while start < end and s[start] == ' ':
#         start = start + 1
#     while end > start and s[end - 1] == ' ':
#         end = end - 1
#     return s[start:end]
# print(trim('   Hello World!       '))
# # for key in dict:
# # for value in d.values():
# # for k,v in d.items():
# # for ch in 'ABC':
# from collections.abc import Iterable
# from collections.abc import Iterable
# isinstance('ABC',Iterable)
# isinstance([1,2,3],Iterable)
# for i,value in enumerate(['A','B','C']): # 获取索引元素对
#     print(i,value)
# def findMinAndMax(L):
#     min = max = None
#     if L:
#         min = max = L[0]
#         for i in L:
#             if i<min:
#                 min=i
#             if i>max:
#                 max = i
#     return (min,max)
# L=[1,0,3,8,5]
# print(findMinAndMax(L))
# print(list(range(1,10)))
# print([x*x for x in range(1,11)])
# print([x*x for x in range(1,11) if x % 2==0])
# print([m+n for m in 'ABC' for n in 'XYZ'])
# import os
# print(d for d in os.listdir('.'))
# # [k+'='+v for k,v in d.items()]
# print([x if x%2 ==0 else -x for x in range(1,11)])
# L = ['Hello', 'World', 18, 'Apple', None]
# print([s.lower() if isinstance(s,str) else s for s in L])
# g = (x*x for x in range (10))
# for i in g:
#     print(i)
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'
# g=fib(6)
# while True:
#     try:
#         x=next(g)
#         print('g:',x)
#     except StopIteration as e:
#         print('Generator return value:',e.value)
#         break

#打印杨辉三角
def triangles(n=10):
    cur_row = [1]
    row_count = 1
    while row_count <= n:
        yield cur_row
        next_row = [1]
        for i in range(len(cur_row)-1):
            next_row.append(cur_row[i]+cur_row[i+1])
        next_row.append(1)
        cur_row = next_row
        row_count += 1

for g in triangles(10):
    print(g)