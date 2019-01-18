import time,os
import unittest
from log.logger_setting import logger,Logger
from common import global_setting
from ele_operation import share_operation
from HTMLTestReportUI import HTMLTestRunner
if __name__ == "__main__":
    Logger.level = "INFO"
    Logger.set_log_format("full")
    Logger.add_handler(global_setting.log_txt_dir)
    logger.info("开始测试" + "\n" + "..........................." + "\n" + "...........................")
    p = share_operation.Share_op()
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    reportdir = global_setting.report_dir
    casedir = global_setting.testcase_dir
    discover = unittest.defaultTestLoader.discover(casedir, pattern="test_tms*.py")
    filename = now + ".html"
    fp = open(os.path.join(reportdir, filename), "wb")
    runner = HTMLTestRunner(stream=fp, title="test")
    runner.run(discover)
    p.close_program()

# unittest.main()
