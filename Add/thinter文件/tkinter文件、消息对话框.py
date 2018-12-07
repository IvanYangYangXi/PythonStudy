#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# thinter文件消息对话框.py
# @Author :  ()
# @Link   : 
# @Date   : 11/29/2018, 11:07:30 AM


import os
import tkinter
import tkinter.filedialog as fil


#==============[文件对话框]================#
# title:标题；mode：'w'/'r',读写模式；initialdir：默认路径，为空则是当前路径；filetypes：文件类型；parent：制定在某个窗口之上；
def func1():
    a =tkinter.filedialog.askopenfilename(title=u'选择文件',initialdir=(os.path.expanduser('C:\\')),filetypes=(("TXT", ".txt"),('所有文件','.*')))#返回文件名
    print(a)
    a =tkinter.filedialog.askopenfile()#返回文件流对象
    print(a)
    a =tkinter.filedialog.askdirectory()#返回目录名
    print(a)
    a =tkinter.filedialog.askopenfilenames()#可以返回多个文件名
    print(a)
    a =tkinter.filedialog.askopenfiles()#多个文件流对象
    print(a)
    a=tkinter.filedialog.asksaveasfilename()#返回文件名
    print(a)
    a =tkinter.filedialog.asksaveasfile()#会创建文件，并返回路径
    print(a)



#================[信息、警告、错误消息框]=======================#
import tkinter.messagebox
def info_warn_err():
    a=tkinter.messagebox.showinfo("我的标题","我的提示1")
    print(a)
    a=tkinter.messagebox.showwarning("我的标题","我的提示2")
    print(a)
    a=tkinter.messagebox.showerror("我的标题", "我的提示3")
    print(a)
def func2():
    a=tkinter.messagebox.askyesno("我的标题","我的提示1")
    print(a)
    a=tkinter.messagebox.askokcancel("我的标题","我的提示2")
    print(a)
    a=tkinter.messagebox.askquestion("我的标题","我的提示3")
    print(a)
    a=tkinter.messagebox.askretrycancel("我的标题","我的提示4")
    print(a)
    a=tkinter.messagebox.askyesnocancel("我的标题","我的提示5")
    print(a)
    #这里用作演示如何使用对话框
    if tkinter.messagebox.askyesno("我的标题", "确认关闭窗口吗!"):
        root.destroy() # 退出TK进程



root = tkinter.Tk()
# root.withdraw() #这里需要注意的是，需要创建一个Tkinter.Tk()实例，然后将其隐藏（root.withdraw(),因为在使用filedialog.askopenfilename()时调用了GUI组件，使用后需要有GUI进程来管理这个句柄。当我们注释掉root = Tkinter.Tk()和root.withdraw()后，再运行这段代码，可以发现filedialog.askopenfilename()后桌面会一直有个Tk窗口，而且处于未响应状态。
btn = tkinter.Button(root,text='click',command=func1)
btn1 = tkinter.Button(root,text="信息、警告、错误消息框",command=info_warn_err)
btn2 = tkinter.Button(root,text="对话框",command=func2)

btn.pack()
btn1.pack()
btn2.pack()

root.mainloop()


#================[Python2.7]===============#

# import Tkinter,tkFileDialog

# root = Tkinter.Tk()
# root.withdraw()

# filename = tkFileDialog.askopenfilename(filetypes=[("bmp","bmp")])
