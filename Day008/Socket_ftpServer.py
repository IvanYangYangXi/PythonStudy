#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Socket_ftpServer.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/4/2018, 11:53:06 AM


import socket ,os ,hashlib

server = socket.socket() # 创建socket连接
# server.bind(('0.0.0.0',9999)) # 绑定ip和端口
server.bind(('localhost',9999))

server.listen() # 开始监听

while True: # 等待客户端连接
    conn, addr = server.accept()  # 若连接成功，返回客户端的ip地址和端口
    print('new conn:',addr) 
    while True:
        print('等待新指令')
        data = conn.recv(1024) # 等待接收客户端数据
        if not data: # 如果返回的data为空，表示客户端断开
            print('客户端已断开')
            break

        print('接收数据',data)
        recv_get,filename = data.decode().split() # 获得文件路径
        print(recv_get,' ',filename) 
        if os.path.isfile(filename):
            f = open(filename,"rb") # 打开文件
            file_size = os.stat(filename).st_size # 获得文件大小
            m = hashlib.md5()
            conn.send(str(file_size).encode()) # send file size
            conn.recv(1024) # wait for respond
            for line in f: # 逐行读发
                m.update(line)
                conn.send(line)
            print('file md5',m.hexdigest())
        else: # 若发送文件为空或不存在
            conn.send(b'0')
            conn.recv(1024)
            conn.send(str('no find file %s'%filename).encode())

        print('send done')

server.close()