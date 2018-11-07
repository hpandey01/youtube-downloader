from pytube import YouTube
import os
import sys
import subprocess
from threading import Thread
from pathlib import Path
import time

def func1(a,name):
	my_file=Path("C:\\ffmpeg\\_files\\"+name+".mp3")
	while True:
		if my_file.is_file():
			time.sleep(60)
			a.kill()
			break


link=input(sys.argv[1])
yt=YouTube(link)
name=input(sys.argv[2])
stream=yt.streams.filter(res="1080p").first()
stream.download(filename=name+"1")
stream=yt.streams.filter(mime_type="audio/mp4").first()
stream.download(filename=name+"2")
proc=subprocess.Popen(">ffmpeg -i "+name+"1.mp4 -i "+name+"2.mp4 -c:v copy -c:a aac -strict experimental "+name+".mp4 && rm "+name+"1.mp4 && rm "+name+"2.mp4")
Thread(target=func1,args=(proc,name,)).start()