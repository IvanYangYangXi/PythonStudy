#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# socketserver_Server.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/4/2018, 5:06:04 PM


import socketserver

# 1、创建一个请求处理类，且继承BaseRequestHandler，并重写父类的handle()； 每个客户端连接都会与之对应实例化一个这个类
class MyRequestHandler(socketserver.BaseRequestHandler):

    # handle 用于处理所有与客户端的交互
    def handle(self):
        while True:
            print("{} wrote:".format(self.client_address[0])) # 打印客户端的IP地址
            self.data = self.request.recv(1024).strip() # 接受数据
            if not self.data:
                print(self.client_address,"客户端断开了")
                break
            print(self.data)
            self.request.sendall(self.data.upper()) # 发送数据

            # try: # 如果上面的方式会报错使用以下方式
            #     self.data = self.request.recv(1024).strip() # 接受数据
            #     print("{} wrote:".format(self.client_address[0])) # 打印客户端的IP地址
            #     if not self.data:
            #         print(self.client_address,"客户端断开了")
            #         break
            #     print(self.data)
            #     self.request.sendall(self.data.upper()) # 发送数据
            # except ConnectionResetError as e :
            #     print('客户端断开了')
            #     break


if __name__ == '__main__':
    HOST, POST = 'localhost',9999

    # 2、实例化TCPServer，并传递server IP 和 上面创建的请求处理类 给这个TCPServer
    # server = socketserver.TCPServer((HOST, POST), MyRequestHandler) # 单线程不支持多并发
    server = socketserver.ThreadingTCPServer((HOST, POST), MyRequestHandler) # 使用多线程, ForkingTCPServer():多进程
    server.serve_forever() # 3、处理多个请求，且永远执行