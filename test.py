import os
import tkinter
import tkinter.filedialog as fil



def func1():
    file_path = fil.askopenfilename() # 打开文件;askopenfilenames() # 打开多个文件
    print(file_path)
    path = fil.askdirectory() # 目录选择
    print(path)
    save_file = fil.asksaveasfile() # 保存文件
    print(save_file)

root = tkinter.Tk()
# root.withdraw() #这里需要注意的是，需要创建一个Tkinter.Tk()实例，然后将其隐藏（root.withdraw(),因为在使用filedialog.askopenfilename()时调用了GUI组件，使用后需要有GUI进程来管理这个句柄。当我们注释掉root = Tkinter.Tk()和root.withdraw()后，再运行这段代码，可以发现filedialog.askopenfilename()后桌面会一直有个Tk窗口，而且处于未响应状态。
btn1 = tkinter.Button(root,text='click',command=func1)
btn1.pack()
root.mainloop()