#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# password.py
# @Author : {__Ivan-杨杨兮__} ({__523166477@qq.com__})
# @Link   : 
# @Date   : 10/14/2018, 2:38:57 PM


import getpass

username = input("username:")
password = getpass.getpass("password:")

repassword = getpass.getpass("RePassword:")

if repassword == '' or password == '':
    print("password or repassword= null")
elif repassword == password:
    print("Ture")
else:
    print("password is not equal")

print(username,password)