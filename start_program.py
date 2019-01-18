import py_operation
import pic_location
import pic_ordermanage
import P_order_query
import time
op = py_operation.operation()
pic = pic_location.start_pic()
pic_order = pic_ordermanage.order_pic()
page_order_query = P_order_query.order_pic()
def start_program():
    op.doubleclick(pic.start_process)
def login(username,pwd):
    start_program()
    op.input(pic.username,username)
    op.input(pic.pwd,pwd)
    op.click(pic.login)

def orderManage():
    a = op.click(pic_order.order)
def order_query(number_type,number,startime,endtime,custid,check):
    op.click(page_order_query.query["button_querymore"])
    page_order_query.number_select(number_type)
    page_order_query.input_number(number)
    page_order_query.input_starttime(startime)
    page_order_query.input_endtime(endtime)
    page_order_query.custid_input(custid)
    page_order_query.click_query()
    if op.is_exist_pic(check):
        print("测试通过")
    else:
        print("测试不通过")
#start_program()
#op.m.click(38,455,1,2)
if __name__ == "__main__":
    try:
        login("admin","123456")
        orderManage()
        order_query("子单号","201812121321","2018-12-12-12-12-12","2018-12-13-13-1-13","100010",page_order_query.query["check"])
    except Exception as e:
        print(e)