import pywin
app = pywin.Pywin()
tool_name = r"E:\test\Nebula.SYS.Client.Apps.ClientHoseApp.exe"
windows_name = "TMS"
username = "Edit1"
pwd = "Edit2"
login = "选择服务器Static"
input_username = "admin"
input_pwd = "123456"
app.run(tool_name)
app.connect(windows_name)
app.input(windows_name,username,input_username)
app.input(windows_name,pwd,input_pwd)
app.click(windows_name,login)
app.print_selector(windows_name)
