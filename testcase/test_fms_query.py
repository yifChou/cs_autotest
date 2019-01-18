import unittest
from common import read_file
from ele_operation.FMS.sys_manage import cust_payway_set
from ele_operation import py_operation
import start_program
import time
import os
from HTMLTestReportYIF import HTMLTestRunner
from ddt import ddt,data,unpack
from common.log_decorator import *
o = py_operation.operation()
excel_name = o.testdata  # 测试数据文件名
rf = read_file.read_excel(excel_name)
testdata = rf.data_to_list("财务系统")
for i in testdata:  # 案列执行
    if i == "系统管理/客户支付方式设置/查询":
        testdata = testdata[i]
        print("用例模块路径" + i + "用例模块路径结束")
        op = cust_payway_set.query()
        start_program.login("admin", "123456")  # 登录
        op.enter_page()  # 进入对应模块
        #print(testdata)
@ddt
class FMSTest(unittest.TestCase):
    def setUp(self):
        pass
    @data(*testdata)
    @log_testnow("正在执行运单查询:")
    def test_paywayquery(self,value):
        print(value)
        if value[1] == "是":
            print("测试")
            print("用例模块路径" + i + "用例模块路径结束")
            print("用例名称" + value[0] + "用例名称结束" )
            op.query_list(value)
            data = o.assert_pic(value[3])
            self.assertEqual(data,1,msg="图片不一致")
    def tearDown(self):
        pass
        print("end")
if __name__ == 'main':
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    print(now)
    reportdir = r"C:\Users\Administrator\PycharmProjects\untitled\report"
    casedir = r"C:\Users\Administrator\PycharmProjects\untitled\testcase"
    discover = unittest.defaultTestLoader.discover(casedir,pattern="test_fms*.py")
    print(discover)
    filename = now + ".html"
    print(filename)
    fp = open(os.path.join(reportdir,filename),"wb")
    runner = HTMLTestRunner(stream = fp,title = "test")
    runner.run(discover)
    #unittest.main()