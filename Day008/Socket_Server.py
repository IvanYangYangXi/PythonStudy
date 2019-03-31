#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Socket_mod.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/3/2018, 12:20:51 PM


import socket ,os

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
        print('执行指令：',data)
        # cmd_res = os.popen(data.decode()).read() # 执行os指令，（使用.popen（）将字符串作为指令执行）
        cmd_res = data.decode()
        print(cmd_res)
        print('before send',len(cmd_res)) # 发送前检查发送数据的长度，若为0则不发送
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."

        conn.send(str(len(cmd_res.encode())).encode('utf-8')) # 先发送数据长度到客户端，要使用bits格式发送
        client_ack = conn.recv(1024) # 检测客户端是否收到，若收到会有数据返回
        print('ack from clint:',client_ack.decode())
        conn.send(cmd_res.encode('utf-8')) # 以bits格式发送数据
        print('send done')

server.close()