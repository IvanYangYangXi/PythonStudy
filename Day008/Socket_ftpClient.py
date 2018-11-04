#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Socket_Client.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/3/2018, 5:29:29 PM


import socket,hashlib

client = socket.socket() # 创建socket实例
client.connect(('localhost',9999)) # 连接到服务器

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0: continue # 若为空则跳出本次循环进入下一次循环
    if cmd.startswith('get'): # startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
        client.send(cmd.encode()) # 发送文件路径
        server_response = client.recv(1024) # 等待服务器返回
        print('sercer response:',server_response) 
        file_total_size = int(server_response.decode()) # 将返回值转为int类型
        client.send(b'ready to recv file') # 回复服务器
        if file_total_size != 0:
            received_size = 0
            filename = cmd.split()[1]
            f = open(filename + '.new','wb') # 二进制写模式
            while received_size < file_total_size:
                data = client.recv(1024)
                received_size += len(data)
                f.write(data)
                print(file_total_size,received_size)
            else:
                print("file recv done",file_total_size,received_size)
                f.close()
        else: print(client.recv(1024).decode('utf-8'))


client.close()