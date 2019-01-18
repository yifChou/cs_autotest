import xlrd
from common import global_setting
class read_excel():
    def __init__(self,file):
        self.workbook = xlrd.open_workbook(filename=file)
        self.sheetnames = self.workbook.sheet_names()
        self.excel_data = {
        }
        self.modoul = []
    def get_moduel(self,sheetname):
        for i in self.sheetnames:
            if i ==sheetname:
                sheet  = self.workbook.sheet_by_name(i)
                #print(sheet.ncols,sheet.nrows)
                dict_data = []
                one_data =[]
                data_num = []
                num = 0
                for row in range(1, sheet.nrows):
                    route = str(sheet.cell(row,0).value)
                    if route =="":
                        num = num + 1
                        if row == sheet.nrows - 1:
                            data_num.append(num)
                    else:
                        data_num.append(num)
                data_num = [data_num[i:i + 2] for i in range(len(data_num)) if i != len(data_num) - 1]
                print("用例条数",data_num)
                flag = -1
                row = 1
                while row <=sheet.nrows:
                    try:
                        route = str(sheet.cell(row,0).value)
                        isexcute = sheet.cell(row, 2).value
                        print(route,isexcute)
                        if route != "":  # 存储参数名称
                            flag = flag + 1
                            if isexcute == "是":
                                cs_list = []
                                # print("改行列数为：",len(sheet.row_values(col)))
                                # print("?????????????", row, sheet.ncols)
                                dict_data.append(route)
                                dict_data.append(data_num[flag])  # 用例条数
                                dict_data.append("casename")
                                dict_data.append(isexcute)
                                dict_data.append("result")
                                dict_data.append("expect")
                                # print("?????????????",row, sheet.ncols)
                                if sheet.ncols > 5:
                                    for col in range(sheet.ncols):
                                        cs = str(sheet.cell(row, col + 5).value)
                                        cs_list.append(cs)
                                        # print("cs",cs)
                                        if col + 6 == sheet.ncols:
                                            dict_data.append(cs_list)
                            else:
                                '''
                                不执行的条数
                                '''
                                datanum = data_num[flag][1]
                                row =datanum + 1
                                print("跳转到",row)

                        else:
                            data_list = []
                            for col in range(sheet.ncols):
                                data = str(sheet.cell(row,col+1).value)
                                data_list.append(data)
                                if col + 2 == sheet.ncols:
                                    one_data.append(data_list)
                        row = row + 1
                    except Exception as e:
                        row = row + 1
                        continue
                a = [dict_data[i:i+7] for i in range(0,len(dict_data),7)]
                print(dict_data,one_data)
                return [a,one_data]
    def data_to_dict(self,sheetname):
        raw_data = self.get_moduel(sheetname)
        #print("数据：",raw_data)
        moduel = raw_data[0] #参数
        da = raw_data[1]     #数据
        for data in moduel:#参数子列表存放到母列表中
            data.extend(data[6])
            del data[6]
        try:
            tem_list = []
            self.excel_data = {}
            for data in moduel:
                for i in range(data[1][0],data[1][1]):
                    a = dict(zip(data[2::],da[i])) #参数列表和数据列表转换成字典
                    tem_list.append(a)
                    if i == data[1][1]-1:#每个模块存储相应的测试数据
                        self.excel_data[data[0]] = tem_list
                        tem_list = []
            #print("字典:",self.excel_data)
            return self.excel_data
        except Exception as e:
            print(e)
    def data_to_list(self,sheetname):
        raw_data = self.get_moduel(sheetname)
        #print("数据：", raw_data[1])
        moduel = raw_data[0]  # 参数
        #print("参数：",moduel)
        da = raw_data[1]  # 数据
        for data in moduel:  # 参数子列表存放到母列表中
            data.extend(data[6])
            del data[6]
        try:
            tem_list = []
            self.excel_data = {}

            for data in moduel:
                print("data:",data)
                num = data[1][1]-data[1][0]
                for i in range(num):
                    #print(da[i])
                    if da[i][1] =="是":
                        #print(da[i])
                        #if da[i][]
                        a = da[i] #数据列表
                        tem_list.append(a)
                    if i == num-1:#每个模块存储相应的测试数据
                        #print(tem_list)
                        self.excel_data[data[0]] = tem_list
                        tem_list = []
            #print("字典:",self.excel_data)
            return self.excel_data
        except Exception as e:
            print(e)

if __name__ == "__main__":
    file = r"C:\Users\Administrator\Desktop\query.xlsx"
    excel = read_excel(global_setting.testdata_dir)
    print(excel.sheetnames)
    sheet = "TMS"
    #print(excel.get_moduel("系统名（WOS系统）"))
    #print(excel.modoul)
    #print(excel.data_to_dict(sheet))
    print(excel.data_to_list(sheet))