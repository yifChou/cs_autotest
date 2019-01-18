from common import read_file
from ele_operation.FMS.sys_manage import cust_payway_set
import start_program
op = cust_payway_set.query()
excel_name = op.op.testdata #测试数据文件名
rf = read_file.read_excel(excel_name)
data = rf.data_to_list("财务系统")
print(type(data))
start_program.login("admin","123456") #登录
op.enter_page() #进入对应模块
for i in data:  #案列执行
    if i== "系统管理/客户支付方式设置/查询":
        for data in data[i]:
            if data[1] == "是":
                print("正在执行用例为：",data[0])
                op.query_list(data)
                print(data[0],"执行完毕")
