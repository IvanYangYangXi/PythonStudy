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
    cmd_res_size = client.recv(2048)  # 接受数据（先接收数据的大小）
    print('接收到的数据的大小：',cmd_res_size)
    client.send("数据大小已收到，准备好接受数据啦".encode('utf-8'))
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)
        received_data += data
    else:
        print('cmd res recevied done.',received_size)
        print(received_data.decode())

client.close()