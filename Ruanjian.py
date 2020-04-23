import json
import tkinter
import requests
from tkinter import *
from tkinter import messagebox

# 获取函数
def result_str():
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    # 获取输入框 entry_content的内容
    content = entry_content.get().strip()  # 输入的内容去除前后的空格

    data = {
        'i': content,
        'doctype': 'json'
    }
    res_string = requests.post(url, headers=header, data=data).content.decode()
    json_data = json.loads(res_string)

    res.set(json_data["translateResult"][0][0]["tgt"])


window = tkinter.Tk()
window.title("中英文互转软件")

window.geometry('400x600+880+20')
label_content = tkinter.Label(text='内容:  ',foreground='red', font=('GB2312', 22))
label_content.grid(row=0, column=0)


entry_content = tkinter.Entry(font=('GB2312', 15))
entry_content.grid(row=0, column=1)

label_output = tkinter.Label(text='输出:  ', foreground='red', font=('GB2312', 22))
label_output.grid()
res = tkinter.StringVar()

entry_output = tkinter.Entry(font=('GB2312', 15),textvariable=res)
entry_output.grid(row=1, column=1)

btn_result = tkinter.Button(text="翻译",width=10,font=('GB2312', 18),command=result_str)
btn_result.grid(row=2, column=0,sticky=W)
btn_quit = tkinter.Button(text="退出",width=10,font=('GB2312', 18), command=window.quit)
btn_quit.grid(row=2, column=1,sticky=E)

window.mainloop()