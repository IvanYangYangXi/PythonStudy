#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# json反序列化.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 10/21/2018, 9:53:21 PM

import json
import pickle

def sayhi(name):
    print("hello ",name)
    print('两边必须有同名函数，但内容可以不一样')


f = open("json_test.txt",'r')
data = json.loads(f.read())
p = open("pickle_test.txt",'rb')
data2 = pickle.loads(p.read()) # == data2 = pickle.load(p)


print(data)
data2("Ivan")