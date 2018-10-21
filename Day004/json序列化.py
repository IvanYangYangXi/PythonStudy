#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# json序列化.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 10/21/2018, 6:35:21 PM


import json # 只能序列化简单类型
import pickle # 可序列化函数，只能在python内部使用

def sayhi(name):
    print("hello ",name)

info = {
    'name':'Ivan',
    'link':'cgartech',
    # 'func':sayhi
}


f = open("json_test.txt",'w')
f.write(json.dumps(info)) 
f = open("pickle_test.txt",'wb')
f.write(pickle.dumps(sayhi)) # == pickle.dump(sayhi,f)
f.close()