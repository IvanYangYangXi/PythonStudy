#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ListAndDictionary.py
# @Author : {__Ivan-杨杨兮__} ({__523166477@qq.com__})
# @Link   : 
# @Date   : 10/18/2018, 8:16:30 PM


# Python之路,Day2 - Python基础2:http://www.cnblogs.com/alex3714/articles/5717620.html

#=====================list=======================#

names = ["A","B",["AA","BB"],"C","D","E"]

# 获取
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


names_b = ["A","B","C","D","G"]
sel = list(set(names).intersection(set(names_b))) # 获取两个list 的交集


names_tuple = ("a","b") # 元组，固定不能改变的列表；只有 .index 、.count 两个方法


#===================Dictionary====================#

# d = {key1 : value1, key2 : value2 }
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组

print("dict['Name']: ", dict['Name']) # 获取‘Name’的值，如果用字典里没有的键访问数据，会输出错误
dict['Age'] = 8 # 修改
dict['School'] = "RUNOOB" # 添加

# cmp(dict1, dict2) # 比较两个字典元素
len(dict) # 计算字典元素个数，即键的总数
dict.copy() # 返回一个字典的浅复制
# dict.has_key(key) # 如果键在字典dict里返回true，否则返回false
if ('lastProject' in dict.keys()): # 判断字典是否存在某个key
    dict['lastProject']
dict.keys() # 以列表返回一个字典所有的键
print(list(dict.keys())) # 转换为列表形式
dict.values() # 以列表返回字典中的所有值
# dict.update(dict2) # 把字典dict2的键值更新到dict1里

del dict['Name']  # 删除键是'Name'的条目
dict.clear()      # 清空词典所有条目
del dict          # 删除词典

