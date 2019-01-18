from ele_operation import py_operation,share_operation
import time
import start_program
class query():
    def __init__(self):
        self.op = py_operation.operation()
        self.pic_root = self.op.get_dir("pic_storage\\fms\\cust_pay_setting")
        self.query = self.op.add_pic(self.pic_root)
        self.list_data = {"organization": ["总公司", "华强北营业部", "坂田营业部", "福州营业部","","徐州营业部","义务分公司"],
                          "sign":["","","","","","","","","","","","深圳前海云途","","深圳云途",""],
                          "group":["","","","业务二部","","","",""],
                          "paystat": ["","已启用","已失效"],
                          "payway": ["","微信","皮卡","在线支付","支付宝"],
                          "deaddate": ["","预付","月结","半月结","周结","现结"],
                          "coin": ["","欧元","英镑","港币","人民币","俄罗斯卢币","新加坡元","美元","日元"],
                          }
    def custid_input(self,content):
        if content != "":
            self.op.find_input(self.query["custid"],self.query["custid_cx"],content,x = 170 , x2=-50)
            self.op.click(self.query["custid_cx"])
            self.op.click(self.query["custid_ok"])
        else:
            self.op.delete_input(self.query["custid"],x = 50)
    def sign_input(self,content):
        self.op.dropdown_box_select(self.query["sign"],list_c=self.list_data["sign"],value=content,x=170,y_spacing=17)
    def organ_input(self,content):
        self.op.dropdown_box_select(self.query["organization"],list_c=self.list_data["organization"],value=content,x=180,y_spacing=17)
    def group_input(self,content):
        self.op.dropdown_box_select(self.query["group"],list_c=self.list_data["group"],value=content,x=170,y_spacing=17)

        pass
    def paystat_input(self,content):
        self.op.dropdown_box_select(self.query["paystat"],list_c=self.list_data["paystat"],value=content,x=180,y_spacing=17)
        pass
    def payway_input(self,content):
        self.op.dropdown_box_select(self.query["payway"],list_c=self.list_data["payway"],value=content,x=185,y_spacing=17)
        pass
    def deaddate_input(self,content):
        self.op.dropdown_box_select(self.query["deaddate"], list_c=self.list_data["deaddate"], value=content, x=170,
                                    y_spacing=17)
        pass
    def coin_input(self,content):
        self.op.dropdown_box_select(self.query["coin"],list_c=self.list_data["coin"],value=content,x=160,y_spacing=17)
    def query_1(self):
        self.op.click(self.query["query"])
        #print("success")
    def enter_page(self):
        self.op.click(self.query["sys"])
        self.op.click(self.query["sys_manage"])
        self.op.click(self.query["cust_payway_setting"])
    def query(self,custid,sign,group,deaddate,coin,paystat,payway,organ):
        op.custid_input(custid)
        op.sign_input(sign)
        op.group_input(group)
        op.deaddate_input(deaddate)
        op.coin_input(coin)
        op.paystat_input(paystat)
        op.payway_input(payway)
        op.organ_input(organ)
        op.query_1()
    def query_list(self,listdata):#参数从第4个index开始
        # ['新增币种', '是', '', 'D:\\picture\\fms\\acc_manage\\expect_result\\add_success.png', 'add', 'add', '', '', '', '', '', '']
        self.custid_input(listdata[4])
        self.organ_input(listdata[5])
        self.sign_input(listdata[6])
        self.group_input(listdata[7])
        self.paystat_input(listdata[8])
        self.payway_input(listdata[9])
        self.deaddate_input(listdata[10])
        self.coin_input(listdata[11])
        self.query_1()

if __name__ == "__main__":
    op = query()
    '''start_program.login("admin","123456")
    op.enter_page()
    op.organ_input("福州营业部")'''
    def query(custid,sign,group,deaddate,coin,paystat,payway,organ):
        op.custid_input(custid)
        op.sign_input(sign)
        op.group_input(group)
        op.deaddate_input(deaddate)
        op.coin_input(coin)
        op.paystat_input(paystat)
        op.payway_input(payway)
        op.organ_input(organ)
    query("100010",'','','','','','','')
    #op.query_1()