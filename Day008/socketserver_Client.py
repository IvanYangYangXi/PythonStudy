#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Socket_Client.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/3/2018, 5:29:29 PM


import socket

client = socket.socket() # 创建socket实例
client.connect(('localhost',9999)) # 连接到服务器

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0: continue # 若为空则跳出本次循环进入下一次循环
    client.send(cmd.encode('utf-8')) # 发送Bits格式数据
    data = client.recv(1024)
    print("recv:",data.decode())

client.close()
