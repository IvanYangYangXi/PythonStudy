#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# os_mod.py
# @Author : {__Ivan-杨杨兮__} ({__523166477@qq.com__})
# @Link   : 
# @Date   : 10/16/2018, 11:02:48 PM


import os

cmd_res = os.system("dir") # windows下，dir 查看当前路径下的文件，结果直接输出到屏幕,不保存结果
print("-->",cmd_res) # cmd_res获得的是返回值，0表示成功

cmd_res2 = os.popen("dir") # 查看当前路径下的文件，并存储结果，通常使用此命令
print("-->",cmd_res2) # 输出是内存地址
print("-->",cmd_res2.read()) # 使用 .read（） 读取内容

os.mkdir("new_dir")
# os.makedirs 创建多级目录