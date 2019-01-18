from ele_operation import py_operation
from common.log_decorator import log_something
from log.logger_setting import logger,Logger
from common import global_setting
import time
class Login():
    def __init__(self):
        pass
        pic_path = r"pic_storage\login"  #图片路径
        self.op = py_operation.operation()
        #self.shareop = share_operation.Share_op()
        self.pic = self.op.add_pic(pic_path) #登录的所有图片变成字典数据
    def username_input(self,content):
        pass
        self.op.input(self.pic["username"],content,x = 20)
    def pwd_input(self,content):
        pass
        self.op.input(self.pic["pwd"], content, x=20)
    def login_click(self):
        self.op.click(self.pic["login"])
    def update(self,ifupdate_pic):
        try:
            self.op.wait_untill_display(ifupdate_pic,t = 2)
            self.op.click(self.pic["nextstep"])
            success = self.op.wait_untill_display(self.pic["finish"])
            if success:
                self.op.click(self.pic["finish"])
            else:
                print("更新异常")
                Logger.error("程序更新异常")
        except Exception :
            print("没有更新")
    def doubclick_fms(self):
        self.op.doubleclick(self.pic["tms"])
    @log_something("尝试登陆系统：")
    def login_sys(self,user,pwd):
        self.doubclick_fms()
        self.username_input(user)
        self.pwd_input(pwd)
        self.login_click()
        self.update(self.pic["update"])

if __name__ == "__main__":
    Logger.level = "DEBUG"
    Logger.set_log_format("full")
    Logger.add_handler(global_setting.log_txt_dir)
    logger.debug("开始测试")
    l = Login()
    start = time.strftime("%Y_%m_%d_%H_%M_%S")
    s = time.time()
    print(start)
    l.login_sys("admin","123456")
    end = time.strftime("%Y_%m_%d_%H_%M_%S")
    e = time.time()
    print(end)
    print("耗时:",e-s)
    #l.shareop.close_program()
