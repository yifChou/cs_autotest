from ele_operation import py_operation
from common import global_setting
from common.log_decorator import *
from log.logger_setting import Logger

class Share_op():
    def __init__(self):
        pass
        #pic_path = "\pic_storage\picture\share"  # 图片路径
        self.op = py_operation.operation()
        self.pic = self.op.add_pic(global_setting.share_op_dir)
        '''
        页面与title关联字典
        '''
        self.pagelist = {
            "运输总单":"transorder",
            "空运提单管理":"airorder",
            "清关提单管理": "clearorder",
            "更新提单数据": "updatedata",
            "客户支付方式设置": "payway",
        }
        # 登录的所有图片变成字典数据
    def username_input(self, content):
        self.op.input(self.pic["username"], content, x=20)
    def pwd_input(self, content):
        self.op.input(self.pic["pwd"], content, x=20)
    def login_click(self):
        self.op.click(self.pic["login"])
    def update(self, ifupdate_pic):
        update = self.op.wait_untill_display(ifupdate_pic, t=2)
        if update:
            self.op.click(self.pic["nextstep"])
            success = self.op.wait_untill_display(self.pic["finish"])
            if success:
                self.op.click(self.pic["finish"])
            else:
                print("更新异常")
                Logger.error("程序更新异常")
        else:
            print("没有更新")
    def doubclick_fms(self):
        self.op.doubleclick(self.pic["tms"])
    @log_something("尝试登陆系统：")
    def login_sys(self, user, pwd):
        try:
            self.doubclick_fms()
            self.username_input(user)
            self.pwd_input(pwd)
            self.login_click()
            self.update(self.pic["update"])
        except:
            raise TimeoutError
    @log_one("关闭系统")
    def close_program(self):
        self.op.click(self.pic["prog_close"],x = 30)

    @log_something("尝试进入页面:")
    def search_enter(self,menu):
        flag = 0
        for pic in self.pagelist:
            if menu == pic:
                flag = 1
                checkpic = self.pic[self.pagelist[pic]]
                isexist = self.op.assert_pic(checkpic)
                if isexist == 1:
                    self.op.click(checkpic)
                else:
                    self.op.click(self.pic["search"])
                    self.op.input(self.pic["query"], menu, x=60)
                    self.op.click(self.pic["query"])
                    self.op.click(self.pic["yes"])

                break
        if flag == 0:
            raise TimeoutError



if __name__ == "__main__":
    s = Share_op()
    s.login_sys("admin","123456")
    s.search_enter("运输总单")
    s.close_program()
    '''
    import time
    
    s.search_enter("运输总单")
    s.search_enter("空运提单管理")
    s.search_enter("清关提单管理")
    s.search_enter("更新提单数据")
    s.search_enter("客户支付方式设置")
    s.search_enter("首页")
    '''

