class order_pic():
    def __init__(self):
        self.root_ordermanage = "D:\\picture\\orderManage\\"
        self.base = self.root_ordermanage + "base.png"
        self.order = self.root_ordermanage + "order.png"
        self.querymore = self.root_ordermanage + "querymore.png"
        self.yewuyuan = {"base":self.root_ordermanage + "base_yewuyuan.png",
                         "jiang":self.root_ordermanage + "yewuyuan_jiang.png",
                         "jiangjie": self.root_ordermanage + "yewuyuan_jiangjie.png"}
        self.kehudaima = {"base":self.root_ordermanage + "base.png",
                         "kehudaima":self.root_ordermanage + "kehudaima.png"}
        self.query = self.root_ordermanage + "query.png"
        self.yewuyuanbig = self.root_ordermanage + "yewuyuanbig.png"
        self.find_input = {"base":self.root_ordermanage + "base_find_input.png",
                         "find_input":self.root_ordermanage + "find_input.png",
                           "query":self.root_ordermanage + "find_query.png",
                           "queding":self.root_ordermanage + "queding.png"}
        self.test = {"base": self.root_ordermanage + "test_base.png",
                     "input": self.root_ordermanage + "input_test.png"}
        self.language = {"base": self.root_ordermanage + "base.png",
                         "base_cn": self.root_ordermanage + "base_chinese.png",
                     "chinese": self.root_ordermanage + "chinese.png",
                         "english":self.root_ordermanage + "en.png",
                         "cn":self.root_ordermanage + "cn.png",}
if __name__ == "__main__":
    pic = order_pic()
    print(pic.yewuyuan["base"])
