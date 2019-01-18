from pymouse import PyMouse
from pykeyboard import PyKeyboard
import opencv_aircv
import time
import pic_location
import pic_ordermanage
import shot_screen2
import os
import logger_setting
import pyautogui
import pyperclip
class operation():
    def __init__(self):
        self.pic = pic_location.start_pic()
        self.m = PyMouse()
        self.k = PyKeyboard()
        self.gui = pyautogui
        self.clip = pyperclip
        self.logger = logger_setting.LoggerSetting()
        self.logger.level = "INFO"
        self.logger.set_log_format("full")
        self.logger.logger_handler("add","D:\\picture\\log.txt")
    #创建文件夹
    def creat_dir(self,checkpic):
        try:
            picname = os.path.split(checkpic)
            newdir = picname[0] + "\\Nofound"
            if not os.path.exists(newdir):
                os.makedirs(newdir)
                self.logger.info("文件夹创建成功：" + newdir)
            return newdir
        except Exception as e:
            self.logger.error("文件创建失败" + newdir)
    #检查下拉框是否存在要选择内容
    def scroll_exist_content(self,checkpic):
        xy = opencv_aircv.check_pic_xy(checkpic)
        if xy is None:
            print("次找不到" + checkpic)
        else:
            return xy
    #判断元素是否存在屏幕
    def is_exist_pic(self,checkpic):
        i = 0.5
        while i <= 2:
            xy = opencv_aircv.check_pic_xy(checkpic)
            if xy is None:
                print("第"+str(int(i)+1) + "次找不到" + checkpic)
                time.sleep(i)
                i = i + 0.5
                if i == 2.5:
                    print("当前页面找不到"+checkpic)
                    picpath = self.creat_dir(checkpic)
                    picname = "\\" + os.path.split(checkpic)[1]
                    print(picpath+picname)
                    shot_screen2.window_capture(picpath+picname)
                    self.logger.error(picpath+picname + "页面不存在该元素:" + checkpic)
                    raise TimeoutError
            else:
                return xy

    #点击控件
    def click(self,checkpic,pianx = 0,piany = 0):
        location_xy = self.is_exist_pic(checkpic)
        if location_xy:
            self.m.click(location_xy[0] + pianx,location_xy[1] + piany,1)
            return location_xy
        else:
            print("click")
    #双击控件
    def doubleclick(self,checkpic,x=0,y=0):
        location_xy = self.is_exist_pic(checkpic)
        if location_xy:
            self.m.click(location_xy[0] + x, location_xy[1] + y,1,2)
            print(location_xy,"双 击")
            time.sleep(0.5)
    #控件输入内容
    def input(self,checkpic,content=None,language=2,x = 0 ,y = 0):
        if content is not None:
            location_xy = self.is_exist_pic(checkpic)
            if location_xy:
                self.m.click(location_xy[0] + x, location_xy[1] + y ,1,2)
                self.language_switch(language)
                self.k.type_string(content)
                time.sleep(0.5)
        else:
            pass
    #下拉框选择
    def dropdown_box_select(self,checkpic,content,value,x_spacing,y_spacing):
        xy = self.click(checkpic, x_spacing, 0)
        #time.sleep(10)
        for i in range(len(content)):
            if content[i] == value:
                print(1)
                self.m.click(xy[0] + x_spacing, xy[1] + (i + 1) * y_spacing, 1, 1)
                self.m.click(407, 580, 1, 1)

    def click_listbox(self,y,n,pianx=0,piany=0):
        self.doubleclick(y)
        time.sleep(0.5)
        box_xy = opencv_aircv.check_pic_xy(n)
        self.m.click(box_xy[0],box_xy[1],1)
        time.sleep(0.5)
    #输入内容并查询
    def find_input(self,checkpic,inputpic,content,language=2,pianx=0,piany=0):
        self.click(checkpic,pianx=pianx)
        self.language_switch(language)
        time.sleep(2)
        self.input(inputpic,content,language,x=piany)
    #清空输入内容
    def delete_input(self,checkpic,x=0,y=0):
        self.doubleclick(checkpic,x,y)
        self.gui.press("backspace")
    #输入法切换
    def language_switch(self,language = 2):
        #language = 1 为中文
        if language == 1:
            cn = opencv_aircv.check_pic_xy(pic_ordermanage.order_pic().language["cn"])
            if cn is None:
                self.k.tap_key(self.k.shift_key)
        else:
            english = opencv_aircv.check_pic_xy(pic_ordermanage.order_pic().language["english"])
            if english is None:
                self.k.tap_key(self.k.shift_key)
        time.sleep(1)
    #时间控件输入
    def datetime_input(self,checkpic,date_time,x,space):
        time = date_time.split("-")
        for i in range(len(time)):
            self.input(checkpic,time[i],x=x+i*space)
    #控件粘贴数据内容（解决无法输入中文问题）
    def paste_content(self,checkpic,content,pianx = 0,piany = 0):
        location_xy = self.is_exist_pic(checkpic)
        if location_xy:
            self.delete_input(checkpic,pianx,piany)
            self.copy_paste(content)
            return location_xy
        else:
            print("click")
    #滚动选择内容：
    def scroll_select(self,startroll,selected,endroll,x=0,y=0):
        location_xy = self.is_exist_pic(startroll)
        if location_xy:
            self.m.click(location_xy[0]+x, location_xy[1]+y, 1)
            while self.scroll_exist_content(endroll) is None:
                selected_xy = self.scroll_exist_content(selected)
                if selected_xy:
                    self.m.click(selected_xy[0], selected_xy[1], 1)
                    break
                else:
                    self.gui.scroll(-10)
            else:
                selected_xy = self.scroll_exist_content(selected)
                self.m.click(selected_xy[0], selected_xy[1], 1)
    #复制粘贴内容
    def copy_paste(self,content):
        self.clip.copy(content)
        self.gui.hotkey("ctrl","v")
    def gui_test(self):
        self.gui.typewrite("我")
    def clip_test(self,content):
        self.clip.copy(content)
        self.gui.hotkey("ctrl","v")
if __name__ == "__main__":
    op = operation()
    #op.paste_content(op.pic.username,"admin",pianx=30)
    #op.input(op.pic.pwd,"123456")
    #op.click(op.pic.login)
    op.scroll_select(op.pic.start_roll,op.pic.sys,op.pic.end_roll)