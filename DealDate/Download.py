import datetime
from tkinter import *
import tkinter
import urllib.request
import threading

#http://img.moredian.com/temporary/2018/4/17/21/deviceLog_010101180319NC3047_.zip

class myThread (threading.Thread):
    def run(self):
        timestr = Entry_time.get()
        snstr = Entry_SN.get()
        tlog(timestr,snstr)

def getstr():
    thread1 = myThread()
    thread1.setDaemon(True)
    thread1.start()

def seturl():
    global url
    if v.get() == '塔上' and envir.get() == "生产环境":
        url = 'http://timg.moredian.com/temporary/'
    elif v.get() == '塔下' and envir.get() == "生产环境":
        url = 'http://img.moredian.com/temporary/'
    if v.get() == '塔上' and envir.get() == "开发环境":
        url = 'http://timg.dev.moredian.com:8000/temporary/'
    elif v.get() == '塔下' and envir.get() == "开发环境":
        url = 'http://img.dev.moredian.com:8000/temporary/'
    if v.get() == '塔上' and envir.get() == "测试环境":
        url = 'http://timg.test.moredian.com:8002/temporary'
    elif v.get() == '塔下' and envir.get() == "测试环境":
        url = 'http://img.test.moredian.com:8002/temporary'
    return url

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    words = "下载中：" + str(round(percent,2)) + "%"
    label["text"] = str(words)

def tlog(time,sn):
    url = seturl()
    url = url+time+'/deviceLog_'+sn+'_.zip'
    try:
        urllib.request.urlretrieve(url, sn + ".zip",callbackfunc)
        words_corrent = '下载完成'
        label["text"] = words_corrent
    except urllib.error.HTTPError as e:
        words = '没有文件'
        label["text"] = words



root = Tk()
root.title('设备日志下载')
root.geometry('500x200')
root.wm_attributes('-topmost', 1)
v = StringVar()
v.set("塔上")
envir = StringVar()
envir.set("生产环境")
e = StringVar()
t = StringVar()

now_time = datetime.datetime.now()
time1_str = str(now_time.year)+'/'+str(now_time.month)+'/'+str(now_time.day)+'/'+str(now_time.hour)
e.set(time1_str)
t.set('090105200414KN1076')

label_env = tkinter.Label(root, text="环境选择",borderwidth=5,width = 5).place(x=150,y=0)
Button1 = Radiobutton(root,text="塔上",variable = v,value = '塔上',command=seturl).place(x=86,y=25)
Button2 = Radiobutton(root,text="塔下",variable = v,value = '塔下',command=seturl).place(x=156,y=25)
Envir_rel = Radiobutton(root,text="生产",variable = envir,value = '生产环境',command=seturl).place(x=86,y=55)
Envir_dev = Radiobutton(root,text="开发",variable = envir,value = '开发环境',command=seturl).place(x=158,y=55)
Envir_test = Radiobutton(root,text="测试",variable = envir,value = '测试环境',command=seturl).place(x=228,y=55)

Entry_SN = Entry(root, borderwidth=1,textvariable=t,width = 20)
Entry_time = Entry(root, borderwidth=1,textvariable=e,width = 20)
text_SN = tkinter.Label(root, text="SN:",width =4,anchor=NW).place(x=86,y=115)
text_time = tkinter.Label(root, text="时间:",width=4,anchor=NW).place(x=86,y=85)
label = tkinter.Label(root, text="您好",width=20,anchor=W)
# labe11 = tkinter.Label(root, text="",width=1).place(x=86,y=145)
comand = Button(root, text="获取", command=getstr, width=10, height=2).place(x=300,y=90)

label.place(x=86,y=145)
Entry_time.place(x=140,y=85)
Entry_SN.place(x=140,y=115)
root.mainloop()


