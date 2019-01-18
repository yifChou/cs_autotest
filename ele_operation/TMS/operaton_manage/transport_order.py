from ele_operation import py_operation
from ele_operation import share_operation
from log.logger_setting import *
class tranport():
    def __init__(self):
        self.op = py_operation.operation()
        self.login = share_operation.Share_op()
        self.pic = self.op.add_pic("pic_storage\\tms\\transport_order")
        self.listdata = {
             "id":["运输总单","袋子号","出货总单","提单号"],
            "time":["创建时间","预计发货时间","预计到达时间"],
            "transtate":["草稿","运输中","完成","作废"],
            "relationstate":["","未关联","已关联"],
            "harbor": ["", "HKAIR", "ZHAIR", "SHAIR", "", "", "", "SC", "", "", "", "", "", "", "", "", "", "", "", "RRR", "QQQ","THJ"],
            "product":["","test"],
            "organization": ["总公司", "华强北营业部", "坂田营业部", "福州营业部", "佛山山水", "上海分公司", "成都分公司","厦门分公司"],
        }
    def enter_page(self):
        self.login.login_sys("admin","123456")
        self.login.search_enter("运输总单")
    '''
    运输总单，单据类型查询
    '''
    def id_input(self,content):
        self.op.dropdown_select(self.pic["id"],self.listdata["id"],"运输总单",x = -380)
        self.op.input(self.pic["id"], content, x=-50)
    def dzid_input(self, content):
        self.op.dropdown_select(self.pic["id"], self.listdata["id"], "袋子号", x=-380)
        self.op.input(self.pic["id"], content, x=-50)
    def zdid_input(self,content):
        self.op.dropdown_select(self.pic["id"],self.listdata["id"],"出货总单",x = -380)
        self.op.input(self.pic["id"], content, x=-50)
    def tdid_input(self, content):
        self.op.dropdown_select(self.pic["id"], self.listdata["id"], "提单号", x=-380)
        self.op.input(self.pic["id"], content, x=-50)

    '''
     发货点输入
     '''
    def delivery_input(self,content):
        self.op.dropdown_box_select(self.pic["delivery"],self.listdata["organization"],content,x= 160,y_spacing=16)
    '''
     新建出货--发货点输入
     '''
    def newdelivery_input(self,content):
        self.op.dropdown_box_select(self.pic["newdelevery"],self.listdata["organization"],content,x= 150,y_spacing=16)

    '''
    时间类型选择
    '''
    def time_type(self,content):
        self.op.dropdown_select(self.pic["time"], self.listdata["time"], content, x=100,y_spacing=16)
    '''
     开始时间输入
     '''
    def time_input_s(self,content):
        self.op.datetime_input(self.pic["time"],content,x = 205)

    '''
     结束时间输入
     '''
    def time_input_e(self,content):
        self.op.datetime_input(self.pic["time"],content,x = 350)

    '''
     运输状态输入
     '''
    def transtate_input(self,content):
        self.op.input(self.pic["transtate"],content, x=50)

    '''
     批次号输入
     '''
    def patch_input(self,content):
        self.op.input(self.pic["patchid"], content, x=50)

    '''
     产品线输入
     '''
    def product_input(self,content):
        self.op.input(self.pic["product"], content, x=50)
        pass
    '''
    提单关联状态输入
    '''
    def relation_input(self,content):
        self.op.input(self.pic["relationstate"], content, x=50)
        pass
    '''
    起始港输入
    '''
    def fromhar_input(self, content):
        self.op.input(self.pic["fromhar"], content, x=50)
    '''
    目的港输入
    '''
    def deshar_input(self, content):
        self.op.input(self.pic["deshar"], content, x=50)
    '''
    收货服务商输入
    '''
    def server_input(self, content):
        self.op.click(self.pic["server"],x = 180)
        self.op.input(self.pic["query"],content,x = 60)
        #self.op.click(self.pic["query"])
        self.op.click(self.pic["comfirm"])
        time.sleep(1)
    '''
        新建服务商输入
    '''
    def newserver_input(self, content):
        self.op.click(self.pic["server"],x = 180)
        self.op.input(self.pic["query"],content,x = 60)
        #self.op.click(self.pic["query"])
        self.op.click(self.pic["queren"])
    '''
    运输总单查询
    '''
    def query_click(self):
       self.op.click(self.pic["query"])
    def query(self,id,idcontent,delivery,timetype,starttime,endtime,transport,patch,product,relation,fromhar,deshar,server):
        if id == "运输总单":
            self.tdid_input(idcontent)
        elif id == "袋子号":
            self.dzid_input(idcontent)
        elif id == "出货总单":
            self.zdid_input(idcontent)
        elif id == "提单号":
            self.tdid_input(idcontent)
        else:
            op.tdid_input("")
        self.delivery_input(delivery)
        self.time_type(timetype)
        self.time_input_s(starttime)
        self.time_input_e(endtime)
        self.transtate_input(transport)
        self.patch_input(patch)
        self.product_input(product)
        self.relation_input(relation)
        self.fromhar_input(fromhar)
        self.deshar_input(deshar)
        self.server_input(server)
        self.query_click()
        pass
    def query_list(self,listdata):
        if listdata[4] == "运输总单":
            self.tdid_input(listdata[5])
        elif listdata[4] == "袋子号":
            self.dzid_input(listdata[5])
        elif listdata[4] == "出货总单":
            self.zdid_input(listdata[5])
        elif listdata[4] == "提单号":
            self.tdid_input(listdata[5])
        else:
            op.tdid_input("")
        self.delivery_input(listdata[6])
        self.time_type(listdata[7])
        self.time_input_s(listdata[8])
        self.time_input_e(listdata[9])
        self.transtate_input(listdata[10])
        self.patch_input(listdata[11])
        self.product_input(listdata[12])
        self.relation_input(listdata[13])
        self.fromhar_input(listdata[14])
        self.deshar_input(listdata[15])
        self.server_input(listdata[16])
        self.query_click()
    def query_order(self,id ,idcontent):
        if id == "运输总单":
            self.id_input(idcontent)
        elif id == "袋子号":
            self.dzid_input(idcontent)
        elif id == "出货总单":
            self.zdid_input(idcontent)
        elif id == "提单号":
            self.tdid_input(idcontent)
        else:
            op.tdid_input("")
        self.query_click()
    def finish(self,id):
        self.query_order(id,"运输总单")
        self.op.click(self.pic["finish"])
        self.op.click(self.pic["ok"])
    '''
    加货
    '''
    def add_goods(self,goods):
        self.op.click(self.pic["selected"])
        isadd = self.op.assert_pic(self.pic["isadd"])
        if isadd == 1:
            self.op.click(self.pic["cancel"])
            self.op.click(self.pic["ok"])
        self.op.click(self.pic["addgoods"])
        self.op.click(self.pic["bagtype"])
        self.op.input(self.pic["addid"],goods,x=40)
        self.op.click(self.pic["addnow"])
        if self.op.is_exist_pic(self.pic["success"]):
            self.op.click(self.pic["close"])
        else:
            print("加货失败")

    '''
    减货
    '''
    def minus_goods(self):
        self.op.click(self.pic["selected"])
        isadd = self.op.assert_pic(self.pic["isadd"])
        if isadd == 1:
            self.op.click(self.pic["cancel"])
            self.op.click(self.pic["ok"])
        self.op.click(self.pic["minusgoods"])
        time.sleep(1)
        self.op.click(self.pic["bagselected"],x = -20)
        self.op.click(self.pic["minusnow"])
        self.op.click(self.pic["yes"])
        self.op.click(self.pic["ok"])
        self.op.click(self.pic["close"])
    def new_order(self,server,patch):
        self.op.doubleclick(self.pic["new"])
        self.server_input(server)
        self.newdelivery_input("总公司")
        self.patch_input(patch)
        self.op.click(self.pic["queding"])
        order = self.op.copy(self.pic["order"],x=60)
        self.op.click(self.pic["close"])
        return order
if __name__ == "__main__":
    Logger.level = "INFO"
    Logger.set_log_format("full")
    Logger.add_handler(global_setting.log_txt_dir)
    logger.info("开始测试" + "\n" + "..........................." + "\n" + "...........................")
    op = tranport()
    pc = share_operation.Share_op()
    #op.enter_page()
    '''op.id_input("111")
    op.dzid_input("222")
    op.zdid_input("2333")
  
    op.tdid_input("444")

    op.delivery_input("华强北营业部")
    op.time_input_s("2018-12-12")
    op.time_input_e("2018-12-26")     

    op.transtate_input("草稿") 
    op.product_input("test")
    op.relation_input("未关联")

    op.server_input("万商")
    pc.login_sys("admin","123456")
    pc.search_enter("运输总单")
    op.time_type("预计到达时间")
    op.query("提单号","123-20181231","总公司","预计到达时间","2018-12-18","2019-01-02","草稿","1213","","已关联","","","三十七服务商")

    op.query_order("运输总单","F-YT-SZ-T-TEST008-190102-03")
    op.add_goods("SV917001526IT")
    op.query_order("运输总单","F-YT-SZ-T-TEST008-190102-03")
    op.minus_goods()
      '''
    order = op.new_order("三十七")
    op.query_order("运输总单",order)
    op.add_goods("SV917001526IT")
    op.finish(order)

