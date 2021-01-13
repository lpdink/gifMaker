# coding: utf-8
from PIL import ImageGrab
import numpy as np
import time
import imageio

def createGif(fps,long,resolve,path):
    fr=1/fps
    end=long
    imageNum = 0
    frames=[]
    starttime=time.time()
    while True:
        imageNum += 1
        captureImage = ImageGrab.grab()  # 抓取屏幕
        captureImage.thumbnail(resolve)
        frame = np.array(captureImage)
        frames.append(frame)
        if imageNum > fps * end:
            break
        time.sleep(fr - ((time.time() - starttime) % fr))
    imageio.mimsave(path+"t1"+".gif", frames, 'GIF',duration=fr)
