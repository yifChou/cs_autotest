from pymouse import PyMouse
from pykeyboard import PyKeyboard
from common import opencv_aircv
import time
import pic_location
import pic_ordermanage
import shot_screen2
import os
from common.log_decorator import *
import pyautogui
import pyperclip
from common import global_setting
import functools
class operation():
    def __init__(self):
        self.pic = pic_location.start_pic()
        self.m = PyMouse()
        self.k = PyKeyboard()
        self.gui = pyautogui
        self.clip = pyperclip
        self.testdata = global_setting.testdata_dir
    #添加页面图片
    @log_one("加载图片到程序")
    def add_pic(self,dirname): #参数为图片文件夹的路径
        dic_pic = {}
        try:
            dirname = self.get_dir(dirname)
            #print(dirname)
            for file in os.listdir(dirname):
                #print(file)
                pic_name = file.split('.')
                if len(pic_name) ==2:
                    if pic_name[1] == "png":
                        tem_dir = os.path.join(dirname,file)
                        dic_pic[pic_name[0]] = tem_dir
            #print(dic_pic)
            return dic_pic
        except:
            logger.error("加载图片失败")
            raise BaseException

    #创建文件夹
    def creat_dir(self,checkpic): #创建Nofound文件夹
        try:
            picname = os.path.split(checkpic)
            newdir = picname[0] + "\\Nofound"
            if not os.path.exists(newdir):
                os.makedirs(newdir)
                logger.info("文件夹创建成功：" + newdir)
            return newdir
        except Exception as e:
            logger.error("文件创建失败" + newdir)
    #检查是否存在要选择内容
    def scroll_exist_content(self,checkpic): #参数为图片的路径
        xy = opencv_aircv.check_pic_xy(checkpic)
        if xy is None:
            #print("次找不到" + checkpic)
            pass
        else:
            return xy
    #判断元素是否存在屏幕
    def is_exist_pic(self,checkpic):#参数为图片的路径
        i = 0.5
        while i <= 2:
            xy = opencv_aircv.check_pic_xy(checkpic)
            if xy is None:
                time.sleep(i)
                i = i + 0.5
                if i == 2.5: #页面找不到元素，截图到对应的nofound文件夹
                    #print("当前页面找不到"+checkpic)
                    picpath = self.creat_dir(checkpic)
                    picname = "\\" + os.path.split(checkpic)[1]
                    #print(picpath+picname)
                    shot_screen2.window_capture(picpath+picname)
                    logger.error(picname + "页面不存在:")
                    raise TimeoutError
            else:
                return xy
    def shot_screen(self,path,picname):
        shot_screen2.window_capture(path + picname)
    @log_result("对比结果：",index=1)
    def assert_pic(self,checkpic,second = 1): #checkpic为图片文件夹的路径,second 为验证等待时间，默认1秒,图片0.2秒验证一次
        i = 0.2
        while i <= second:
            xy = opencv_aircv.check_pic_xy(checkpic)
            if xy is None:
                #print("第"+str(int(i)+1) + "次找不到" + checkpic)
                time.sleep(i)
                i = i + 0.2
                if i == second:
                    #print("当前页面找不到"+checkpic)
                    picpath = self.creat_dir(checkpic)
                    picname = "\\" + os.path.split(checkpic)[1]
                    #print(picpath+picname)
                    shot_screen2.window_capture(picpath+picname)
                    logger.error("页面不存在:" + picname)
                    return 0
            else:
                return 1

    #点击控件
    def click(self,checkpic,x = 0,y = 0): #checkpic为图片文件夹的路径,x为X轴偏移正数向右负数像左，y为Y轴偏移正数向右负数像左，默认不偏移
        location_xy = self.is_exist_pic(checkpic)
        if location_xy:
            #print(location_xy)
            self.m.click(location_xy[0] + x,location_xy[1] + y,1)
            time.sleep(0.5)
            return location_xy
        else:
            print("click")
    #双击控件
    def doubleclick(self,checkpic,x=0,y=0):#checkpic为图片文件夹的路径,x为X轴偏移正数向右负数像左，y为Y轴偏移正数向右负数像左，默认不偏移
        location_xy = self.is_exist_pic(checkpic)
        if location_xy:
            self.m.click(location_xy[0] + x, location_xy[1] + y,1,2)
            #print(location_xy,"双 击")
            time.sleep(0.5)
    #控件输入内容
    @log_op(text="文本输入：",index=2)
    def input(self,checkpic,content=None,x = 0 ,y = 0):#content字符输入，输入内容
        if content is not None:
            location_xy = self.is_exist_pic(checkpic)
            if location_xy:
                self.paste_content(checkpic,content,x,y)
                time.sleep(0.5)
        else:
            pass

    def input_time(self,checkpic,content=None,x = 0 ,y = 0):#content字符输入，输入内容
        if content is not None:
            location_xy = self.is_exist_pic(checkpic)
            if location_xy:
                self.m.click(location_xy[0]+x,location_xy[1]+y)
                self.k.type_string(content)
                time.sleep(0.1)
        else:
            pass
    #下拉框选择-可以输入内容的下拉框
    @log_op(text="下拉选择：", index=3)
    def dropdown_box_select(self,checkpic,list_c,value,x,y_spacing = 0):
        #list_c为下拉框的所有内容数组，value为要选择的下拉框内容，x点击下拉按钮偏移，y_spacing为Y轴间隔偏移
        self.delete_drownbox_content(checkpic,x-30)
        xy = self.click(checkpic,x)
        #time.sleep(3) #调试鼠标所在位置
        flag = 0
        for i in range(len(list_c)):
            if list_c[i] == value:
                self.m.click(xy[0] +x, xy[1] + (i + 1) * y_spacing, 1, 1)
                time.sleep(3)
                flag = 1
                break
        if flag:
            return 1
        else:
            return 0
                #time.sleep(3)
    #下拉框--不能输入类型的下拉框
    @log_op(text="下拉选择->", index=3)
    def dropdown_select(self,checkpic,list_c,value,x,y_spacing = 17):
        xy = self.click(checkpic,x)
        #self.delete_content(checkpic,x+60)
        #time.sleep(3) #调试鼠标所在位置
        flag = 0
        for i in range(len(list_c)):
            if list_c[i] == value:
                self.m.click(xy[0] + x, xy[1] + (i + 1) * y_spacing, 1, 1)
                #self.m.click(407, 580, 1, 1)
                #time.sleep(3)
                flag = 1
                break
        if flag:
            return 1
        else:
            return 0

    def click_listbox(self,y,n,pianx=0,piany=0):
        self.doubleclick(y)
        time.sleep(0.5)
        box_xy = opencv_aircv.check_pic_xy(n)
        self.m.click(box_xy[0],box_xy[1],1)
        time.sleep(0.5)
    #输入内容并查询
    #@log_op(text="输入查询：", index=3)
    def find_input(self,checkpic,inputpic,content,x=0,x2=0):
        #针对可查询的输入框，checkpic为查询的输入框，inputpic为查询页面的输入框位置，x =为checkpic的偏移，x2为inputpic的偏移
        self.click(checkpic,x=x)
        self.wait_untill_display(inputpic)
        self.input(inputpic,content,x=x2)
    #清空输入内容
    def delete_input(self,checkpic,x=0,y=0):
        xy = self.click(checkpic,x,y)
        self.gui.hotkey("ctrl","a")
        self.gui.press("backspace")
        return xy
    #删除下拉框选项
    def delete_drownbox_content(self,checkpic,x=0,y=0):
        xy = self.click(checkpic, x, y)
        #self.gui.hotkey("ctrl","a")
        self.gui.press("backspace")
        return xy
    def delete_content(self,checkpic,x=0,y=0):
        xy = self.click(checkpic, x, y)
        self.gui.hotkey("ctrl","a")
        self.gui.press("backspace")
        return xy
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
    @log_op(text="日期输入：", index=2)
    def datetime_input(self,checkpic,date_time,x,space = 16):
        # date_time为要输入的时间格式为“2018-12-15-12-00-00”，x为x偏移，space为月日时分秒的间隔偏移
        if date_time != "":
            time = date_time.split("-")
            for i in range(len(time)):
                self.input_time(checkpic,time[i],x=x+i*space)
    #控件粘贴数据内容（解决无法输入中文问题）
    def paste_content(self,checkpic,content,x = 0,y = 0):
        #content为粘贴内容
        location_xy = self.is_exist_pic(checkpic)
        if location_xy:
            self.delete_input(checkpic,x,y)
            self.copy_paste(content)
            return location_xy
        else:
            print("click")
    #滚动选择内容：
    def scroll_select(self,startroll,selected,endroll,x=0,y=0):
        #startroll 滚动条在最上方截图路径，endroll滚动条在最下方截图路径，selected被选中内容的图片路径
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
    def copy(self,checkpic,x = 0 ,y = 0):
        self.click(checkpic,x = x,y =y)
        self.gui.hotkey("ctrl", "a")
        self.gui.hotkey("ctrl","c")
        return self.clip.paste()
        pass
    @log_op(text="等待页面出现：", index=1)
    def wait_untill_display(self,checkpic,t = 5):
        #在规定时间内等待元素是否出现，t为等待时长，默认5秒
        for i in range(t):
            isexist = self.assert_pic(checkpic)
            if isexist:
                return 1
            else:
                if i == t -1:
                    return 0
                else:
                    time.sleep(1)
                    continue
    #获取pic_storage图片路径
    def get_dir(self,picdir):
        return  global_setting.get_dir(picdir)
    def get_my_dir(self,my,picdir):
        dir = os.getcwd()
        new = dir[0:dir.find(my)]
        return  os.path.join(new + picdir)
    def gui_test(self):
        self.gui.hotkey("enter")
    def clip_test(self,content):
        self.clip.copy(content)
        self.gui.hotkey("ctrl","v")
if __name__ == "__main__":
    dir = "D:\\picture\\orderManage\\query\\"
    op = operation()
    '''#op.paste_content(op.pic.username,"admin",pianx=30)
    #op.input(op.pic.pwd,"123456")
    #op.click(op.pic.login)
    #op.scroll_select(op.pic.start_roll,op.pic.sys,op.pic.end_roll)
    op.logger.debug("123")
    op.logger.error("456")
    op.add_pic(dir)'''




    op.gui_test()