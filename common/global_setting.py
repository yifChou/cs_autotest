import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Home_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
share_op_dir = os.path.join(Home_Dir,"pic_storage\share" )
log_txt_dir = os.path.join(Home_Dir,"log\log.txt")
testdata_dir = os.path.join(Home_Dir,'testdata\\testdata.xlsx')
report_dir = os.path.join(Home_Dir,'report')
testcase_dir = os.path.join(Home_Dir,'testcase')
capture_dir = os.path.join(Home_Dir,"pic_storage\\test1.png")
def get_dir(path):
    dir = os.path.join(Home_Dir,path)
    return dir
if __name__ == "__main__":
    print(log_txt_dir,"\n",testdata_dir)