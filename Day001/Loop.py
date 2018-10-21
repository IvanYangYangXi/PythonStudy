#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Loop.py
# @Author : {__Ivan-杨杨兮__} ({__523166477@qq.com__})
# @Link   : 
# @Date   : 10/14/2018, 3:06:37 PM


count = 0
while True:
    print("count:",count)
    count = count + 1
    if count == 1000:
        break # 打断并结束循环


count1 = 0
while count1 <1000:
    count1 = count1 +1
else:
    print("count1",count1)


for i in range(10):
    print("loop:",i)


for i in range(10):
    print("loop:",i)
    if i ==9:
        print("break",i)
        break
else: # 循环正常走完则执行，若中途被break打断则不执行
    print("Over",i)



for i in range(1,10,3): # range(循环开始值，循环结束值，循环间隔)
    print("loop:",i)


for i in range(1,10):
    if i<3:
        print("Loop",i)
    else:
        continue # 打断并进入下一次循环
    print("hehe..")


for index,i in enumerate(range(2,10)): # enumerate 获取下标（循环次数，从0开始）
    print(index,'\t',i)