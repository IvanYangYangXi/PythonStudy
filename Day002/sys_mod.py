#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# sys_mod.py
# @Author : {__Ivan-杨杨兮__} ({__523166477@qq.com__})
# @Link   : 
# @Date   : 10/16/2018, 10:55:38 PM


import sys,time

print(sys.path) # sys.path 环境变量
print(sys.argv) # sys.argv 获得相对路径
# print(sys.argv[1]) # 须从控制台运行，获得第1个元素（从0开始）,Sys.argv[ ]其实就是一个列表，里边的项为用户输入的参数，关键就是要明白这参数是从程序外部输入的，而非代码本身的什么地方，要想看到它的效果就应该将程序保存了，从外部来运行程序并给出参数（如：sys_mod.py a b c）。

print(sys.getdefaultencoding()) # sys.getdefaultencoding() 获取系统默认编码

# sys.path.append(path) # 临时添加环境变量

for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush() # .flush 强制刷新，默认是等缓存满后刷新
    time.sleep(.2)