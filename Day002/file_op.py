#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# file_op.py
# @Author : {__Ivan-杨杨兮__} ({__523166477@qq.com__})
# @Link   : 
# @Date   : 10/19/2018, 9:40:34 PM


import sys,os,shutil

print(sys.argv)

f = open('yesterday2','r+',encoding="utf-8")

print(f.readline())

f.write("aaaaaaaaaaaaa\n")
f.write("=============,\n")
f.write("bbbbbbbbbbbb\n")

print(f.tell()) # 获取光标位置
f.seek(0) # 设置光标位置

for index,line in enumerate(f):
    print(index,'\t',line)

f.close()


# 修改文件，必须通过两个文件去操作
f = open('e:\\2018\PythonStudy\Day002\yesterday','r',encoding="utf-8")
f_new = open('yesterday.bak','w',encoding="utf-8")

for line in f:
    if "不知为何" in line:
        line = line.replace("不知为何","不知为何======")
    f_new.write(line)

f.close()
f_new.close()

shutil.copy("e:\\2018\PythonStudy\yesterday2",".\Day002\yesterday3") # 复制文件，可重命名，（.move（）移动文件）
os.remove('e:\\2018\PythonStudy\Day002\yesterday') # 删除文件
os.rename("e:\\2018\PythonStudy\yesterday.bak","e:\\2018\PythonStudy\Day002\yesterday") # 文件重命名，且可以用于移动文件


# with open（……） as ... 通过格式自动关闭文件，一行代码过长使用 \ 换行
with open('yesterday2','r',encoding="utf-8") as f,\
open('yesterday','r',encoding="utf-8") as f2: 
    print(f,'\n',f2.read(50))