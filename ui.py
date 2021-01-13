# 引入库
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import getVedio

# 初始化窗口
window = tk.Tk()
window.title("录制gif")
window.resizable(0, 0)
inputWidth_1 = 20
inputWidth_2 = 20
# 输入Frame
inputFrame = tk.LabelFrame(window, text="Input", font=("黑体", 12))
# inputFrame.rowconfigure(1,weight=1)
inputFrame.columnconfigure(2, weight=1)
# 输入信息
com = ttk.Combobox(inputFrame)  # #创建下拉菜单
com.grid(row=0, column=1, padx=5, sticky=tk.W)  # #将下拉菜单绑定到窗体
com["value"] = ("15", "30", "60")  # #给下拉菜单设定值
com.current(1)
label1 = tk.Label(inputFrame, text="录制帧数").grid(row=0, column=0, sticky=tk.W)  # padx=0)
label2 = tk.Label(inputFrame, text="快捷键").grid(row=0, column=3, sticky=tk.E)
entry2 = tk.Label(inputFrame, text="F10")
entry2.grid(row=0, column=4, sticky=tk.E)
label3 = tk.Label(inputFrame, text="最长录制时间(秒)").grid(row=1, column=0, sticky=tk.W)  # padx=0)
s1 = tk.Scale(inputFrame, from_=3, to=60, orient=tk.HORIZONTAL)
s1.grid(row=1, column=1, padx=5, sticky=tk.W)
label5 = tk.Label(inputFrame, text="分辨率").grid(row=2, column=0, sticky=tk.W)  # padx=0)
com2 = ttk.Combobox(inputFrame)  # #创建下拉菜单
com2.grid(row=2, column=1, padx=5, sticky=tk.W)  # #将下拉菜单绑定到窗体
com2["value"] = ("480*360", "640*480", "1280*720", "1920*1080")  # #给下拉菜单设定值
com2.current(1)
path3 = tk.StringVar()
label7 = tk.Label(inputFrame, text="保存gif路径").grid(row=3, column=0, sticky=tk.W)  # padx=0)
entry7 = tk.Entry(inputFrame, textvariable=path3, show=None, width=inputWidth_2)
entry7.grid(row=3, column=1, padx=5, sticky=tk.W)
inputFrame.grid(row=0, stick=tk.NSEW)


def loadFile3():
    # 传入需要修改的entry

    filePath = filedialog.askdirectory()
    path3.set(filePath)


loadFile3_button = tk.Button(inputFrame, text="选择文件夹", font=('黑体', 10), command=loadFile3).grid(row=3, column=2,
                                                                                                sticky=tk.E)
fps=int(com.get())
long=int(s1.get())
com2Str=com2.get()
com2Index=com2Str.find('*')
resolve=(int(com2Str[0:com2Index]),int(com2Str[com2Index+1:]))
print(resolve)
path=str(entry7.get())
button_play =tk.Button(window, text="开始/结束", bg='#fff000',font=('黑体', 10),height=5,width=30,
                       command=lambda :getVedio.createGif(int(com.get()),int(s1.get()),
                                                          (int(com2.get()[0:com2Str.find('*')]),int(com2.get()[com2Str.find('*')+1:])),
                                                          str(entry7.get()))).grid(row=5, column=0, sticky=tk.NSEW)

window.mainloop()
