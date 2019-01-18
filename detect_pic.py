import pytesseract
from PIL import Image
import requests
import os
import time
import opencv_aircv
dir = "D:\\12306\\"
url = "https://kyfw.12306.cn/passport/captcha/captcha-image?"
def detect_word(dir,name):
    im = Image.open(dir + name)
    return pytesseract.image_to_string(im,lang="chi_sim")
    #tesseract D:\picture\sys.png
def download_pic(url,picname):
    r = requests.get(url)
    with open(dir+picname,'wb') as f:
        f.write(r.content)
        return dir+picname
    pass
#需要验证的标签
def cut_pic(dir,savedir,savename):
    img = Image.open(dir)
    cut_img = img.crop((118,0,180,40))
    cut_img.save(savedir+savename)
    pass
#验证码剪裁成8个图片
def cut_8pics(dir,savedir):
    img = Image.open(dir)
    #1图片长73，高70
    length = 70
    high = 70
    delay = 10
    cut_img = img.crop((delay, 40, length, high+40))
    cut_img.save(savedir + "01.png")
    #2
    cut_img = img.crop((length+delay,40, length*2, high + 40))
    cut_img.save(savedir + "02.png")
    # 3
    cut_img = img.crop((length*2+delay, 40, length*3, high + 40))
    cut_img.save(savedir + "03.png")
    # 4
    cut_img = img.crop((length * 3+delay, 40, length * 4, high + 40))
    cut_img.save(savedir + "04.png")
    #5
    cut_img = img.crop((delay, 40+high, length, high*2 + 40))
    cut_img.save(savedir + "05.png")
    # 6
    cut_img = img.crop((length+delay, 40+high, length * 2, high*2 + 40))
    cut_img.save(savedir + "06.png")
    # 7
    cut_img = img.crop((length * 2+delay, 40+high, length * 3, high*2 + 40))
    cut_img.save(savedir + "07.png")
    # 8
    cut_img = img.crop((length * 3+delay, 40+high, length * 4, high*2 + 40))
    cut_img.save(savedir + "08.png")
    pass
def cut_8_namepics(dir,savedir,name):
    img = Image.open(dir)
    #1图片长73，高70
    length = 70
    high = 70
    delay = 10
    cut_img = img.crop((delay, 40, length, high+40))
    cut_img.save(savedir + name +"01.png")
    #2
    cut_img = img.crop((length+delay,40, length*2, high + 40))
    cut_img.save(savedir + name +"02.png")
    # 3
    cut_img = img.crop((length*2+delay, 40, length*3, high + 40))
    cut_img.save(savedir + name +"03.png")
    # 4
    cut_img = img.crop((length * 3+delay, 40, length * 4, high + 40))
    cut_img.save(savedir + name +"04.png")
    #5
    cut_img = img.crop((delay, 40+high, length, high*2 + 40))
    cut_img.save(savedir + name +"05.png")
    # 6
    cut_img = img.crop((length+delay, 40+high, length * 2, high*2 + 40))
    cut_img.save(savedir + name +"06.png")
    # 7
    cut_img = img.crop((length * 2+delay, 40+high, length * 3, high*2 + 40))
    cut_img.save(savedir + name +"07.png")
    # 8
    cut_img = img.crop((length * 3+delay, 40+high, length * 4, high*2 + 40))
    cut_img.save(savedir + name +"08.png")
    pass
#download_pic(url)
def collect_pic():
    for i in range(15):
        try:
            img = str(i+1)+".png"
            pic = download_pic(url,img)
            time.sleep(2)
            cut_dir = dir+str(i+1)+"\\"
            if not os.path.exists(cut_dir):
                os.makedirs(cut_dir)
            #cut_8pics(pic,cut_dir)
            cut_pic(pic,cut_dir,"name_"+str(i)+".png")
        except Exception as e:
            print(e)
            continue
def collect_pic_one(end,start = 0):
    for i in range(start,end):
        try:
            img = str(i+1)+".png"
            pic = download_pic(url,img)
            time.sleep(2)
            #cut_8_namepics(pic,dir,str(i+1))
            cut_pic(pic,dir,"name_"+str(i+1)+".png")
        except Exception as e:
            print(e)
            continue

#cut_8pics(download_pic(url,"1.png"),dir)
def check_repeat():
    for i in range(50):
        for j in range(8):
            print("第" + str(i + 1) + "0" + str(j + 1) + "轮对比")
            try:
                pic_dir = dir + str(i+1)+"0"+str(j+1)+".png"
                for k in range (1,49):
                    for m in range(8):
                        pic2_dir = dir + str(k+1)+"0"+str(m+1)+".png"
                        if is_repeat(pic_dir,pic2_dir):
                            print(pic2_dir,pic_dir)
            except Exception as  e:
                print(e)
                continue
def is_repeat(pic,pic2):
    a = opencv_aircv.check_pic_xyz(pic,pic2)
    b = opencv_aircv.check_pic_xyz(pic,pic2)
    if a and b:
        return 1
    else:
        return 0
    pass
def big_pic(dir,name,big):
    img = Image.open(dir+name)
    w,h = img.size
    im = img.resize((int(big*w),int(big*h)))
    im.save(dir+"big_" + name)
#collect_pic_one(50)
def detect():
    for i in range(50):
        try:
            name = "big_name_" + str(i+1) + ".png"
            print(str(i+1) + ":" + detect_word(dir,name))
        except Exception as e:
            print(e)
            continue
def big(big):
    for i in range(50):
        try:
            name = "name_" + str(i+1) + ".png"
            big_pic(dir,name,big)
        except Exception as e:
            print(e)
            continue
collect_pic_one(50)
