#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# generator生成器.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 10/21/2018, 11:39:43 AM


# 列表生成式，迭代器&生成器： https://www.cnblogs.com/alex3714/articles/5765046.html

def gen(max):
    n,a,b = 0,0,1
    print("n=",n)

    while n < max:
        c = yield # 暂停并返回yield,无返回值时，返回“None”
        # yield b # 暂停并返回b
        a,b = b,a+b
        n = n+1
        print("b=",b)
        print("c=yield=",c)
    return "---done---" # 用于异常返回

f = gen(5)
tryN = 0
f.__next__()
while True:
    try:
        tryN = tryN+1
        print("tryN:",tryN)
        f.send(tryN) # 发送参数到yield，并跳转到yield 标记位置继续执行
        # x = f.__next__() # == next(f) ,跳转到yield 标记位置继续执行
        # print("next(f):",x)
        
    except StopIteration as e: # 异常处理方法，遇到StopIteration 异常执行
        print("StopIteration:",e.value)
        break

# print("yield返回值：",f.__next__())
# print("yield返回值：",f.__next__())
# print("yield返回值：",f.__next__())
# print("yield返回值：",f.__next__())
# print("yield返回值：",f.__next__())
# print("yield返回值：",f.__next__())