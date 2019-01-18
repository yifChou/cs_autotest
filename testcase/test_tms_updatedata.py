import unittest
from  ddt import ddt,data
from ele_operation.TMS.airport_manage import updata_data
from ele_operation.TMS.operaton_manage import transport_order
from common import read_file
from common.log_decorator import *
from ele_operation import  share_operation
op = updata_data.updatedata()
transop = transport_order.tranport()
sop = share_operation.Share_op()
'''
sop.login_sys("admin","123456")
sop.search_enter("更新提单数据")
sop.search_enter("运输总单")'''
file = op.op.testdata  # 测试数据文件名
rf = read_file.read_excel(file)
testdata = rf.data_to_list("TMS")
print(testdata)
for i in testdata:  # 案列执行
    if i == "空运管理/更新提单数据/查询":
        test1 = testdata[i]
        print(test1)
    elif i == "空运管理/更新提单数据/更新加货数据":
        test2 = testdata[i]
        print(test2)
    elif i == "空运管理/更新提单数据/更新减货数据":
        test3 = testdata[i]
        print(test3)
test1 = ""
@ddt
class FMS_coinmanage(unittest.TestCase):
    def setUp(self):
        pass
    @data(*test1)
    @log_testnow("正在执行查询:")
    def test_tms_query(self, value):
        try:
            if value[1] == "是":
                print("测试")
                print("用例模块路径" + i + "用例模块路径结束")
                print("用例名称" + value[0] + "用例名称结束" )
                op.query_list(value)
                data = op.op.assert_pic(op.op.get_dir(value[3]))
                if data == 0:
                    #print("空")
                    a = value[3]
                    name = a[a.find("expect\\") + 7:]
                    path = a[0:a.find("expect\\") + 7]
                    dir = op.op.get_dir(path)
                    op.op.shot_screen(dir,"error_" + name)
                op.click_ok()
                print("结果")
                self.assertEqual(data,1,msg="图片不一致")
        except Exception as e :
            print(e)
            op.click_ok()
    @data(*test2)
    @log_testnow("正在执行更新加货数据:")
    def test_add_update(self, value):
        sop.search_enter("运输总单")
        #order = transop.new_order(value[7],value[8])
        transop.query_order(id = "运输总单",idcontent=value[4])
        goods = value[6].split(",")
        for good in goods:
            transop.add_goods(good)
            transop.finish(value[4])
            if goods.index(good) !=0:
                sop.search_enter("更新提单数据")
                op.queryid(id="运输总单",idcontent=value[4])
                op.click_update()


    @data(*test3)
    @log_testnow("正在执行更新减货数据:")
    def test_minus_update(self, value):
        sop.search_enter("运输总单")
        # order = transop.new_order(value[7],value[8])
        transop.query_order(id="运输总单", idcontent=value[4])
        goods = len(value[6])
        for good in range(goods):
            transop.minus_goods()
            transop.finish(value[4])
            if good != 0:
                sop.search_enter("更新提单数据")
                op.queryid(id="运输总单", idcontent=value[4])
                op.click_update()

    def tearDown(self):
        print("end")