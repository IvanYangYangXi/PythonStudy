#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# threading_ex1.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/4/2018, 9:13:34 PM

# 多线程 信号量

import threading, time


def run2(n):
    semaphore.acquire()
    print('task %s'%n)
    time.sleep(2)
    semaphore.release()


if __name__== "__main__":
    semaphore = threading.BoundedSemaphore(5) # .BoundedSemaphore(5) 信号量，最多允许5个线程同时运行
    for i in range(50):
        tt = threading.Thread(target=run2,args=('tt-%s'%i,))
        tt.start()

# for t in t_objs:
#     t.join() # 等待子线程结束，再继续主线程
while threading.active_count() != 7: # .active_count() 获取当前线程数量，不等于1表示还有子线程存在 (经测试，mac上起来就7个线程，不知道是和原因)
    print(threading.active_count())
    time.sleep(.5)

print('all threads has finished. ')