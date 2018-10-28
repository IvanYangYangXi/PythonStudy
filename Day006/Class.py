#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Class.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 10/28/2018, 11:48:13 AM


# class people: # 经典类写法
class people(object): # 新式类写法
    def __init__(self,name,age,lifevalue=100): # 初始化类（必须包含self）
        self.name = name
        self.age = age
        self.__lifevalue = lifevalue # 前缀“__”表示私有，在外部不能访问

    def showname(self):
        print("people's name is:%s"%(self.name))

    def __del__(self):
        print("销毁对象%s"%(self.name)) # 程序结束时自动执行


class man(people): # 继承类
    def __init__(self,name,age,money): # 重写类
        # people.__init__(self,name,age) # 载入父类的内容（经典写法）
        super(man,self).__init__(name,age) # 载入父类的内容（新式写法）

        self.money = money
        print("%s has %s money"%(self.name,self.money))


m1 = man("Ivan",25,1000000) # == man(m1,"Ivan",25,1000000) 实例化类
m1.showname()
