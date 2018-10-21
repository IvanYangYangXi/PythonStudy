#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# DataType.py
# @Author : {__Ivan-杨杨兮__} ({__523166477@qq.com__})
# @Link   : 
# @Date   : 10/17/2018, 10:23:03 PM



# 数据类型分为string（字符串）和bytes（二进制）
# .encode（‘utf-8’）将字符串转为二进制
# .decode（‘utf-8’）将二进制转为字符串

msg = "我爱天安门"

print(msg)

print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))

print('€20'.encode('utf-8'))
print(b'\xe2\x82\xac20'.decode('utf-8'))

n1 = input("输入字符串或数字：")
if n1.isdigit():  # .isdigit 判断是否为数字
    n1 = int(n1)
    print("输入是数字")
else:
    print("输入为非数字")