import aircv
import pic_location
import shot_screen2

def check_pic_xy(str_check_file,str_base_file="D:\\picture\\orderManage\\base.png", var_find=None, num_resolution_x=None, num_resolution_y=None, num_confidence=0.9, num_base_x=0, num_base_y=0):
    # base是大图,check是小图,能找到图片的完整路径
    obj_base = aircv.imread(shot_screen2.window_capture(str_base_file))

    #obj_base = aircv.imread(str_base_file)
    obj_check = aircv.imread(str_check_file)
    # 分辨率x,y
    if num_resolution_x:
        num_use_x = int(int(num_resolution_x)/obj_base.shape[1])
    else:
        num_use_x = 1
    if num_resolution_y:
        num_use_y = int(int(num_resolution_y)/obj_base.shape[0])
    else:
        num_use_y = 1
    list_tmp = list()
    # 最后得到的坐标x,y和识别准确率
    var_out = None
    # 如果存在多个可以设置使用第几个匹配到的
    try:
        if var_find:
            if var_find != "all":
                var_tmp = aircv.find_all_template(obj_base, obj_check, float(num_confidence))[int(var_find)]
            else:
                var_tmp = aircv.find_all_template(obj_base, obj_check, float(num_confidence))
        else:
            var_tmp = aircv.find_template(obj_base, obj_check, float(num_confidence))
        if var_tmp:
            if type(var_tmp) == dict:
                list_tmp.append(var_tmp)
            else:
                list_tmp = var_tmp
            list_out = list()
            for dict_value in list_tmp:
                # num_base_x,num_base_y是基础偏移,默认不偏移
                list_out.append([int(num_base_x + dict_value["result"][0] * num_use_x), int(num_use_y + dict_value["result"][1] * num_use_y), dict_value["confidence"]])
            if len(list_out) == 1:
                var_out = list_out[0]
            else:
                var_out = list_out
        return var_out
    except Exception as e:
        print(e)
        return 0
def check_pic_xyz(str_check_file,str_base_file, var_find=None, num_resolution_x=None, num_resolution_y=None, num_confidence=0.9, num_base_x=0, num_base_y=0):
    # base是大图,check是小图,能找到图片的完整路径
    obj_base = aircv.imread(str_base_file)

    #obj_base = aircv.imread(str_base_file)
    obj_check = aircv.imread(str_check_file)
    # 分辨率x,y
    if num_resolution_x:
        num_use_x = int(int(num_resolution_x)/obj_base.shape[1])
    else:
        num_use_x = 1
    if num_resolution_y:
        num_use_y = int(int(num_resolution_y)/obj_base.shape[0])
    else:
        num_use_y = 1
    list_tmp = list()
    # 最后得到的坐标x,y和识别准确率
    var_out = None
    # 如果存在多个可以设置使用第几个匹配到的
    try:
        if var_find:
            if var_find != "all":
                var_tmp = aircv.find_all_template(obj_base, obj_check, float(num_confidence))[int(var_find)]
            else:
                var_tmp = aircv.find_all_template(obj_base, obj_check, float(num_confidence))
        else:
            var_tmp = aircv.find_template(obj_base, obj_check, float(num_confidence))
        if var_tmp:
            if type(var_tmp) == dict:
                list_tmp.append(var_tmp)
            else:
                list_tmp = var_tmp
            list_out = list()
            for dict_value in list_tmp:
                # num_base_x,num_base_y是基础偏移,默认不偏移
                list_out.append([int(num_base_x + dict_value["result"][0] * num_use_x), int(num_use_y + dict_value["result"][1] * num_use_y), dict_value["confidence"]])
            if len(list_out) == 1:
                var_out = list_out[0]
            else:
                var_out = list_out
        return var_out
    except Exception as e:
        print(e)
        return 0
# 例子
if __name__ == "__main__":
    dir = ""
    pic = pic_location.start_pic()
    if check_pic_xy(pic.pwd):
        print(1)
    else:
        print(2)
    #print(check_pic_xy(pic.base,pic.pwd))
