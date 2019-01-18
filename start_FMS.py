from pywinauto import Application
app = Application().start(r"E:\test\Nebula.SYS.Client.Apps.ClientHoseApp.exe")
app = Application().connect(title_re = "TMS")
