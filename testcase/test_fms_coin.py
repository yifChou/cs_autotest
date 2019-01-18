import unittest
from  ddt import ddt,data
from ele_operation.FMS.acc_manage import coin_manage
from HTMLTestReportUI import HTMLTestRunner
from common import read_file
from common.log_decorator import *
op = coin_manage.coin_management()
op.enter_page()
file = op.op.testdata  # 测试数据文件名
rf = read_file.read_excel(file)
testdata = rf.data_to_list("财务系统")
#print(testdata)
for i in testdata:  # 案列执行
    if i == "账户管理/币种管理/币种新增":
        test1 = testdata[i]
        print(test1)
    elif i == "账户管理/币种管理/币种查询":
        test2 = testdata[i]
        print(test2)

@ddt
class FMS_coinmanage(unittest.TestCase):
    def setUp(self):
        pass
    @data(*test1)
    @log_testnow("正在执行币种新增:")
    def test_coinadd(self,value):
        print(value)
        if value[1] == "是":
            print("测试")
            print("用例模块路径" + i + "用例模块路径结束")
            print("用例名称" + value[0] + "用例名称结束" )
            op.add_list(value)
            data = op.op.assert_pic(value[3])
            op.op.click(op.add_pic["ok"])
            op.op.click(op.add_pic["add_close"])
            self.assertIsNotNone(data,msg="图片不一致")
    @data(*test2)
    @log_testnow("正在执行币种查询:")
    def test_coinquery(self, value):
        print(value)
        if value[1] == "是":
            print("测试")
            print("用例模块路径" + i + "用例模块路径结束")
            print("用例名称" + value[0] + "用例名称结束")
            op.query_list(value)
            data = op.op.assert_pic(value[3])
            op.click_ok()
            self.assertIsNotNone(data, msg="图片不一致")
    def tearDown(self):
        pass
        print("end")