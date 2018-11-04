#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# threading_ex1.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 11/4/2018, 9:13:34 PM

# 多线程

import threading, time

def run(n):
    print('task %s\n'%n)
    time.sleep(2)


start_time = time.time()
t_objs = [] # 存放线程实例
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    # t.setDaemon(True) # 把当前线程设置为守护线程；此行必须在.start()前
    t.start()
    t_objs.append(t) # 把线程添加到数组中

for t in t_objs:
    t.join() # 等待子线程结束，再继续主线程

print('all threads has finished. cost:',time.time() - start_time)
