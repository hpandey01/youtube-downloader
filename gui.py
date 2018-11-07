from pytube import YouTube
import os
import subprocess
from pathlib import Path
from tkinter import *
import sys
from threading import Thread
import time
import shutil

root = Tk()
root.title("Youtube-MP3 Converter")
frame=Frame(root, width=960, height=540)
frame.config(bg="#595959")
frame.pack()

audio=IntVar()
audio.set(1)
video=IntVar()
video.set(0)
display=StringVar()

def func2():
    display.set("Downloading...")
    
def func1(a):
    my_file = Path("C:\\ffmpeg\\_files\\dist\\youtube\\"+tbox2.get()+".mp3")
    while True:
        if my_file.is_file():
            a.kill()
            time.sleep(5)
            display.set("Downloaded")
            break

def download():
    if video.get()==1:
        os.chdir("C:\\ffmpeg\\_files\\dist\\youtube")
        proc1=subprocess.Popen("youtube.py "+tbox1.get()+" "+tbox2.get())
        Thread(target=func1,args=(proc1,)).start()
        Thread(target=func2).start()

    if audio.get()==1:
         os.chdir("C:\\ffmpeg\\_files\\dist\\youtube")
        proc1=subprocess.Popen("audio-downloader.py "+tbox1.get()+" "+tbox2.get())
        Thread(target=func1,args=(proc1,)).start()
        Thread(target=func2).start()
    
title=Label(text="WELCOME TO YOUTUBE DOWNLOADER")
title.config(font="Arial 18 bold", background="#595959", foreground="#f4f4fa")
title.place(x=219.7, y=10, height=28.6, width=584)

link = Label(text="Video Link: ")
link.config(font="Arial 16 bold",background="#595959", foreground="#ff5500")
link.place(x=53.6, y=88.3, height=33.2, width=127.3)

tbox1 = Entry(frame)
tbox1.config(font="Arial 16")
tbox1.place(x=240, y=88.3, height=33.2, width=600)

name = Label(text="Name Of Video: ")
name.config(font="Arial 16 bold",background="#595959", foreground="#ff5500")
name.place(x=43.6, y=148.3,height=33.2,width=187.3)

tbox2 = Entry(frame)
tbox2.config(font="Arial 16")
tbox2.place(x=240, y=148.3, height=33.2, width=600)

check1=Checkbutton(text= "Audio", variable=audio, onvalue=1, offvalue=0)
check1.place(x=277.9, y=206.375, height=31.25, width=162.2)
check1.config(font="Arial 14 bold", background="#595959", foreground="#ff5500")

check2=Checkbutton(text= "Video", variable=video, onvalue=1, offvalue=0)
check2.place(x=477.9, y=206.375, height=31.25, width=162.2)
check2.config(font="Arial 14 bold", background="#595959", foreground="#ff5500")

button1 = Button(frame, text="DOWNLOAD", command=download)
button1.config(font="Arial 18 bold", foreground="white", background="#fa0604")
button1.place(x=370.7, y=300, height=39.9, width=194.1)

status=Label(textvariable=display)
status.config(font="Arial 18 italic", background="#595959", foreground="#f4f4fa")
status.place(x=180.7, y=400, height=28.6, width=584)

root.mainloop()