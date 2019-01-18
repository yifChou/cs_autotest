from pywinauto import application
import time

class Pywin(object):
    """
    pywin framwork main class
    tool_name : 程序名称，支持带路径
    windows_name : 窗口名字
    """
    SLEEP_TIME = 1

    def __init__(self):
        """
        初始化方法，初始化一个app
        """
        self.app = application.Application()

    def run(self, tool_name):
        """
        启动应用程序
        """
        self.app.start(tool_name)
        time.sleep(3)

    def connect(self, window_name):
        """
        连接应用程序
        app.connect_(path = r"c:\windows\system32\notepad.exe")
        app.connect_(process = 2341)
        app.connect_(handle = 0x010f0c)
        """
        self.app.connect(title_re = window_name)
        time.sleep(1)

    def close(self, window_name):
        """
        关闭应用程序
        """
        self.app[window_name].Close()
        time.sleep(1)

    def max_window(self, window_name):
        """
        最大化窗口
        """
        self.app[window_name].Maximize()
        time.sleep(1)

    def menu_click(self, window_name, menulist):
        """
        菜单点击
        """
        self.app[window_name].MenuSelect(menulist)
        time.sleep(1)

    def input(self, window_name, controller, content):
        """
        输入内容
        """
        self.app[window_name][controller].type_keys(content)
        time.sleep(1)

    def click(self, window_name, controller):
        """
        鼠标左键点击
        example:
        下面两个功能相同,下面支持正则表达式
        app[u'关于“记事本”'][u'确定'].Click()
        app.window_(title_re = u'关于“记事本”').window_(title_re = u'确定').Click()
        """
        self.app[window_name][controller].click()
        time.sleep(1)

    def double_click(self, window_name, controller, x = 0,y = 0):
        """
        鼠标左键点击(双击)
        """
        self.app[window_name][controller].DoubleClick(button = "left", pressed = "",  coords = (x, y))
        time.sleep(1)

    def right_click(self, window_name, controller, order):
        """
        鼠标右键点击，下移进行菜单选择
        window_name : 窗口名
        controller：区域名
        order ： 数字，第几个命令
        """
        self.app[window_name][controller].RightClick()
        for down in range(order):
                time.sleep(0.5)
        time.sleep(1)
    def print_selector(self,window_name):
        self.app[window_name].print_control_identifiers()
