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
    print('task ',n)
    time.sleep(2)

t1 = threading.Thread(target=run,args=('t1',))
t2 = threading.Thread(target=run,args=('t2',))

t1.start()
t2.start()