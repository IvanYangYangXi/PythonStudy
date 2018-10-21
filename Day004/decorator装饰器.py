#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# decorator装饰器.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 10/20/2018, 11:29:34 PM


def deco(func):
    def wrapper(*args, **kwargs): # wrapper = func_x , *args,**kwargs用于存储func_x的参数, *args 列表，**kwargs 字典
        func_return = func(*args, **kwargs)
        return func_return # 返回 func_x 的返回值
    return wrapper

@deco # @deco == func_x=deco(func_x)=wrapper
def func_a():
    print("this is func_a")

@deco
def func_b(name):
    print("this is func_b","name=",name)
    return name


# func_a=deco(func_a) # func = func_a, func_a = wrapper
func_a()
print(func_b("nameb"))