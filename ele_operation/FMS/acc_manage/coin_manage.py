from ele_operation import py_operation
from ele_operation.login import login
import os
class coin_management():
    def __init__(self):
        self.op = py_operation.operation()
        page_dir = "pic_storage/fms/acc_manage" #C:\Users\Administrator\PycharmProjects\svntest
        add_dir = "pic_storage/fms/acc_manage/add" #C:\Users\Administrator\PycharmProjects\svntest
        self.login = login.Login()
        self.page_pic = self.op.add_pic(page_dir)
        self.add_pic = self.op.add_pic(add_dir)
        self.list_data = {
            "coin":["","欧元","英镑","港币","人民币","俄罗斯卢布","新加坡元","新加坡元","台币","美元,","日元","泰铢"],
            "state":["","已失效","待启用","已启用"]
        }
    def coin_input(self,content):
        self.op.dropdown_box_select(self.page_pic["cointype"],self.list_data["coin"],content,x = 140 ,y_spacing=16)
        pass
    def state_input(self,content):
        self.op.dropdown_box_select(self.page_pic["state"],self.list_data["state"],content,x = 140 ,y_spacing=18)

        pass
    def query(self,coin,state):
        self.coin_input(coin)
        self.state_input(state)
        self.op.click(self.page_pic["query"])
        pass

    def query_list(self,listdata):
        self.coin_input(listdata[4])
        self.state_input(listdata[5])
        self.op.click(self.page_pic["query"])
        pass
    def query_ok(self,coin,state):
        self.coin_input(coin)
        self.state_input(state)
        self.op.click(self.page_pic["query"])
        self.click_ok()
        pass
    def click_ok(self):
        isexist = self.op.assert_pic(self.page_pic["tip_nofound"])
        if isexist:
            self.op.click(self.page_pic["ok"])
        else:
            pass
    def enter_page(self):
        self.login.login_sys("admin","123456")
        self.op.click(self.page_pic["sys"])
        self.op.click(self.page_pic["acc_manage"])
        self.op.click(self.page_pic["coin_manage"])
    def add_coin_input(self,content):
        self.op.input(self.add_pic["add_coin"],content,x = 50)
        pass
    def add_coinid_input(self,content):
        self.op.input(self.add_pic["add_coinid"], content, x=90)
        pass
    def add(self,coin,coinid):
        self.op.click(self.page_pic["add"])
        self.add_coin_input(coin)
        self.add_coinid_input(coinid)
        self.op.click(self.add_pic["add_save"])
        pass
    def add_list(self,listdata):
        self.op.click(self.page_pic["add"])
        self.add_coin_input(listdata[4])
        self.add_coinid_input(listdata[5])
        self.op.click(self.add_pic["add_save"])
    def enalbe_coin(self,coin,state):
        self.query(coin,state)
        self.op.click(self.page_pic["enable"])
        self.op.click(self.page_pic["ok"])
        self.click_ok()
        self.query(coin, "已启用")

        pass
    def unalbe_coin(self, coin, state):
        self.query(coin,state)
        self.op.click(self.page_pic["unable"])
        self.op.click(self.page_pic["ok"])
        self.click_ok()
        self.query(coin, "已失效")
    def enter_log(self):
        self.op.click(self.page_pic["log"])
        pass

if __name__ == "__main__":
    op = coin_management()
    #op.enter_page()
    op.enalbe_coin("欧元","已失效")
    op.unalbe_coin("欧元", "已启用")
    print(os.getcwd())