#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# threading_ex1.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/4/2018, 9:13:34 PM

# 多线程 锁

import threading, time


lock = threading.Lock()
def run(n):
    lock.acquire() # .acquire() 获取一把锁
    print('task %s'%n)
    lock.release() # 释放锁
    time.sleep(2)

start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.start()


# for t in t_objs:
#     t.join() # 等待子线程结束，再继续主线程
while threading.active_count() != 7: # .active_count() 获取当前线程数量，不等于1表示还有子线程存在 (经测试，mac上起来就7个线程，不知道是和原因)
    print(threading.active_count())
    time.sleep(.5)

print('all threads has finished. cost:',time.time() - start_time)