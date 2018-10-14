#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# interaction.py
# @Author : {__Ivan-杨杨兮__} ({__523166477@qq.com__})
# @Link   : 
# @Date   : 10/14/2018, 1:40:24 PM

# >>交互 input

'''
python2.x中使用“ raw_input ”代替“ input ”
python2.x中的 input 表示输入变量，而非变量的值
'''

username = input("username:")
password = input("password:")
print(username,password)

testInt = int(input("Input Int:")) # 输入非字符串类型须指定输入类型
testFloat = float(input("Input Float:"))

print(type(testInt) , type( str(testFloat) ))

info = '''
--------info of %s--------
username:%s
password:%s
int:%d
float:%f
'''%(username,username,password,testInt,testFloat)

print(info)

info2 = '''
--------info of {_username}--------
username:{_username}
password:{_password}
int:{_int}
float:{_float}
'''.format(_username=username,
    _password=password,
    _int=testInt,
    _float=testFloat)

print(info2)

info3 = '''
--------info of {0}--------
username:{0}
password:{1}
int:{2}
float:{3}
'''.format(username,password,testInt,testFloat)

print(info3)