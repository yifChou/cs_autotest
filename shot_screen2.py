import time
import numpy as np
from PIL import ImageGrab
# 每抓取一次屏幕需要的时间约为1s,如果图像尺寸小一些效率就会高一些
def window_capture(file):
  img = ImageGrab.grab()
  img.save(file)
  return file
