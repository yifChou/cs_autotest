import py_operation
from pymouse import PyMouse
import time
class order_pic():
    def __init__(self):
        self.op = py_operation.operation()
        self.m = PyMouse()
        self.root_ordermanage = "D:\\picture\\orderManage\\query\\"
        self.base = self.root_ordermanage + "base.png"
        self.query = {
            "button_inner_query":self.root_ordermanage + "button_inner_query.png",
            "input_number": self.root_ordermanage + "input_number" + ".png",
            "button_query": self.root_ordermanage + "button_query" + ".png",
            "button_querymore": self.root_ordermanage + "button_querymore" + ".png",
            "listbox_time": self.root_ordermanage + "listbox_time" + ".png",
            "listbox_saleman": self.root_ordermanage + "listbox_saleman" + ".png",
            "listbox_product": self.root_ordermanage + "listbox_product" + ".png",
            "input_signin": self.root_ordermanage + "input_signin" + ".png",
            "input_signout": self.root_ordermanage + "input_signout" + ".png",
            "listbox_followstate": self.root_ordermanage + "listbox_followstate" + ".png",
            "input_custid": self.root_ordermanage + "input_custid" + ".png",
            "input_prodid": self.root_ordermanage + "input_prodid" + ".png",
            "input_channelid": self.root_ordermanage + "input_channelid" + ".png",
            "listbox_goodstype": self.root_ordermanage + "listbox_goodstype" + ".png",
            "input_serviceid": self.root_ordermanage + "input_serviceid" + ".png",
            "listbox_opstate": self.root_ordermanage + "listbox_opstate" + ".png",
            "listbox_transfertype": self.root_ordermanage + "listbox_transfertype" + ".png",
            "listbox_ischannel": self.root_ordermanage + "listbox_ischannel" + ".png",
            "input_destination": self.root_ordermanage + "input_destination" + ".png",
            "listbox_custservice": self.root_ordermanage + "listbox_custservice" + ".png",
            "listbox_belong": self.root_ordermanage + "listbox_belong" + ".png",
            "listbox_mechanism": self.root_ordermanage + "listbox_mechanism" + ".png",
            "checkbox_c": self.root_ordermanage + "checkbox_c" + ".png",
            "button_ok": self.root_ordermanage + "ok" + ".png",
            "yes": self.root_ordermanage + "yes" + ".png",
            "check": self.root_ordermanage + "check" + ".png",
                      }
        self.list_data = { "number":["单号","子单号","子单跟踪号","历史单号"]
        }
        #self.query_button = {"button_query": self.root_ordermanage + "button_query" + ".png",}
    def number_select(self,value):
        self.op.dropdown_box_select(self.query["button_query"],self.list_data["number"],value,x_spacing=-425,y_spacing=20,)
    def click_query(self):
        self.op.click(self.query["button_query"])
        self.op.click(self.query["button_ok"])
        time.sleep(2)
    def input_starttime(self,datetime):
        self.op.datetime_input(self.query["listbox_time"],datetime,x = 165,space=16)
    def input_endtime(self,datetime):
        self.op.datetime_input(self.query["listbox_time"],datetime,x = 345,space=16)
    def input_number(self,number):
        self.op.input(self.query["button_query"],content=number,x=-370)
    def delete(self):
        self.op.delete_input(self.query["button_query"],x=-370)
    def custid_input(self,content,input_method=0):
        if input_method!=0 :
            self.op.find_input(self.query["input_custid"],self.query["button_inner_query"],content=content,pianx=160,piany=80)
            self.op.click(self.query["button_inner_query"])
            self.op.click(self.query["yes"])
        else:
            self.op.input(self.query["input_custid"],content=content,x=50)
if __name__ == "__main__":
    order = order_pic()
    #order.input_starttime("2018-12-12-13-14-18")
    #order.input_endtime("2018-12-17-8-17-14")
    order.number_select("子单号")
    order.input_number("201812121321")
    order.custid_input("100010")
    order.click_query()
    order.delete()


