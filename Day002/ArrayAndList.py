#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ArrayAndList.py
# @Author : {__Ivan-杨杨兮__} ({__523166477@qq.com__})
# @Link   : 
# @Date   : 10/18/2018, 8:16:30 PM


# Python之路,Day2 - Python基础2:http://www.cnblogs.com/alex3714/articles/5717620.html

names = ["A","B",["AA","BB"],"C","D","E"]

print(names)
print(names[1],names[2])
print(names[1:3])
print(names[-2])
print(names[-3:-1])
print(names[-3:])
print(names[2][0])

names.append("F") # .append 追加
print('\n',names)

names.insert(1,"A1") # .instert 插入
print(names)


names.remove("A1") # .remove 删除
print('\n',names)

names.pop(1) # .pop() 删除，默认删最后一个
print(names)

del names[0] # 删除
print(names)

print(names.index("D")) # .index 索引，获取下标
print(names[names.index("D")])

names.insert(1,"C")
print(names.count("C")) # .count 统计指定项个数

names.reverse() # .reverse 翻转
print(names)

# names.sort() # .sort排序 ;有子序列时，不能进行排序
print(names)

for i in names:
    print(i)

print("\n",names[0:-1:2]) # 间隔取值(0,和-1可以省略：names[::2])


names_tuple = ("a","b") # 元组，固定不能改变的列表；只有 .index 、.count 两个方法
