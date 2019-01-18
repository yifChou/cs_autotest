from ele_operation import py_operation
from ele_operation.login import login
from common import global_setting
import os
import time
class updatedata():
    def __init__(self):
        self.op = py_operation.operation()
        self.login =login.Login()
        #self.pic_enter = self.op.get_dir
        self.pic_enter = self.op.add_pic("pic_storage\\tms")
        self.pic_update = self.op.add_pic("pic_storage\\tms\\airtransp_manage\\update_data")
        self.listdata = {
            "id":["提单号","运输总单"],
            "updatestate":["","未更新","已更新"],
            "transtate":["","草稿","运输中","完成","作废"],
            "harbor":["","","","","",  "","","SC","","",  "","","","","",  "","","","","RRR",  "QQQ","THJ"]
        }
    def tdid_input(self,content):
        self.op.dropdown_select(self.pic_update["id"],self.listdata["id"],"提单号",x=-170,y_spacing=16)

        self.op.input(self.pic_update["id"],content,x=-30)

    def ysid_input(self,content):
        self.op.dropdown_select(self.pic_update["id"],self.listdata["id"],"运输总单",x=-170,y_spacing=16)

        self.op.input(self.pic_update["id"],content,x=-30)

    def patch_input(self,content):
        self.op.input(self.pic_update["patch_id"], content, x=50)
        pass
    def time_input_s(self,content):
        self.op.datetime_input(self.pic_update["time"],content,x = 65)
        pass
    def time_input_e(self,content):
        self.op.datetime_input(self.pic_update["time"],content,x = 255)
        pass
    def updatestate_input(self,content):
        self.op.dropdown_box_select(self.pic_update["update_state"], self.listdata["updatestate"], content, x=160, y_spacing=16)
        pass
    def transtate_input(self,content):
        self.op.dropdown_box_select(self.pic_update["transp_state"], self.listdata["transtate"], content, x=150, y_spacing=16)
        pass
    def fromhar_input(self,content):
        self.op.dropdown_box_select(self.pic_update["from_harbor"], self.listdata["harbor"], content, x=165, y_spacing=17)
        pass
    def deshar_input(self,content):
        self.op.dropdown_box_select(self.pic_update["des_harbor"], self.listdata["harbor"], content, x=150, y_spacing=17)
        pass
    def query_click(self):
       self.op.click(self.pic_update["query"])
    def enter_page(self):

        self.login.login_sys("admin", "123456")
        self.op.click(self.pic_enter["tms"])
        self.op.click(self.pic_enter["airport_manage"])
        self.op.click(self.pic_enter["updata_data"])
    def query(self,id,idcontent,patch = "",starttime= "",endtime= "",updatedata= "",transport= "",fromhar= "",deshar= ""):
        if id == "提单号":
            self.tdid_input(idcontent)
        elif id == "运输总单":
            self.ysid_input(idcontent)
        else:
            self.tdid_input("")
        self.patch_input(patch)
        self.time_input_s(starttime)
        self.time_input_e(endtime)
        self.updatestate_input(updatedata)
        self.transtate_input(transport)
        self.fromhar_input(fromhar)
        self.deshar_input(deshar)
        self.query_click()
        pass
    def query_list(self,listdata):
        if listdata[4] == "提单号":
            self.tdid_input(listdata[5])
        elif listdata[4] == "运输总单":
            self.ysid_input(listdata[5])
        else:
            self.tdid_input("")
        self.patch_input(listdata[6])
        self.time_input_s(listdata[7])
        self.time_input_e(listdata[8])
        self.updatestate_input(listdata[9])
        self.transtate_input(listdata[10])
        self.fromhar_input(listdata[11])
        self.deshar_input(listdata[12])
        self.query_click()
        pass
    def click_update(self):
        self.op.click(self.pic_update["selected"])
        self.op.click(self.pic_update["update"])
    def click_ok(self):
        isexist = self.op.assert_pic(self.pic_update["tip_nofound"])
        if isexist:
            self.op.click(self.pic_update["ok"])
        else:
            pass
    def queryid(self,id,idcontent):
        if id == "提单号":
            self.tdid_input(idcontent)
        elif id == "运输总单":
            self.ysid_input(idcontent)
        else:
            self.tdid_input("")
        self.query_click()
if __name__ == "__main__":
    op = updatedata()
    #print(op.pic_update)
    '''op.tdid_input("123-20181225")
    op.ysid_input("123-20181225")
    op.patch_input("111")
    op.updatestate_input("")
    op.transtate_input("完成")
    op.transtate_input("作废")
    op.transtate_input("草稿")
    op.transtate_input("运输中")
    op.transtate_input("")
    op.fromhar_input("RRR")
    op.fromhar_input("QQQ")
    op.deshar_input("RRR")
    op.deshar_input("QQQ")
    op.fromhar_input("SC")
    op.deshar_input("SC")
    op.time_input_s("2016-12-12-12-12-12")
    op.time_input_e("2016-12-12-12-12-12")
    op.query()
    op.enter_page()
    op.tdid_input("123-20181225")'''
    op.tdid_input("")
    op.query_click()
    op.click_ok()