from pytube import YouTube
import os
import sys
import subprocess
from threading import Thread
from pathlib import Path
import time

def func1(a,name):
	my_file=Path("C:\\ffmpeg\\_files\\downloader\\"+name+".mp4")
	while True:
		if my_file.is_file():
			time.sleep(60)
			a.kill()
			os.remove(name+".mp4")
			break

link=input(sys.argv[1])
yt=YouTube(link)
name=input(sys.argv[2])
stream=yt.streams.filter(mime_type="audio/mp4").first()
stream.download(filename=name)
proc=subprocess.Popen("ffmpeg -i "+name+".mp4 "+name+".mp3 && rm "+name+".mp4")
Thread(target=func1,args=(proc,name,)).start()