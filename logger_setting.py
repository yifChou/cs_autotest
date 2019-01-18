"""
日志模块对应的脚本
"""
# -*- coding: utf-8 -*-
__Another__ = "yif"
import logging
import time


class LoggerSetting:
    """
    @public: 自定义日志
    """

    def __init__(self, log_level_str="INFO"):
        """
        @private: 自执行函数
        @param log_level_str: 日志级别默认INFO,这里不设置也可以
        """
        self.__logger_obj = logging.getLogger("yif" + str(time.time()))
        self.__handler_dict = dict()
        self.__log_level = log_level_str
        self.__obj_formatter = logging.Formatter("[%(message)s]")

    def __str__(self):
        return "自定义日志模块"

    def __call__(self, log_level_str):
        self.__log_level = log_level_str

    def set_log_format(self, log_format_str=None):
        """
        @public: 设置日志格式
        @param log_format_str: 日志显示格式full,half,None
        @return: 无
        """
        if log_format_str == "full":
            self.__obj_formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] [%(module)s] "
                "[%(funcName)s] [%(lineno)d] [%(message)s]")
        elif log_format_str == "half":
            self.__obj_formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(message)s]")
        else:
            # 自定义格式
            self.__obj_formatter = logging.Formatter(log_format_str)
        for handle_obj in self.__handler_dict.values():
            handle_obj.setFormatter(self.__obj_formatter)

    @property
    def level(self):
        """
        @public: 读取日志级别
        @return:
        """
        return self.__log_level

    @level.setter
    def level(self, log_level_str):
        """
        @public: 设置日志等级
        @param log_level_str: 日志等级
        @return: 无
        """

        def set_custom_logger():
            self.__logger_obj.setLevel(log_level_str)
            self.__log_level = log_level_str

        def set_default_logger():
            self.__logger_obj.setLevel("ERROR")
            self.__log_level = "ERROR"

        log_level_dict = dict()
        log_level_dict["NOTSET"] = set_custom_logger
        log_level_dict["DEBUG"] = set_custom_logger
        log_level_dict["INFO"] = set_custom_logger
        log_level_dict["WARN"] = set_custom_logger
        log_level_dict["ERROR"] = set_custom_logger
        log_level_dict["CRITICAL"] = set_custom_logger
        log_level_dict.get(log_level_str.upper(), set_default_logger)()

    def logger_handler(self, log_mode="add", log_write_file=None,
                       handler_level_str="NOTSET", encoding_str="utf-8"):
        """
        @public: 新增或删除日志记录方式
        @param log_mode: 日志操作模式add或del
        @param log_write_file: 不传则为屏幕操作,传文件则是文件操作
        @param encoding_str: 文件编码格式
        @param handler_level_str: 给handler定义日志级别只能显示的比logger少,优先logger的日志级别
        @return: 无
        """

        def set_handler():
            def set_custom_handler():
                log_handler_obj.setLevel(handler_level_str)

            def set_default_handler():
                log_handler_obj.setLevel("ERROR")

            if handler_name != "stream":
                log_handler_obj = logging.FileHandler(log_write_file, encoding=encoding_str)
            else:
                log_handler_obj = logging.StreamHandler()
            handler_level_dict = dict()
            handler_level_dict["NOTSET"] = set_custom_handler
            handler_level_dict["DEBUG"] = set_custom_handler
            handler_level_dict["INFO"] = set_custom_handler
            handler_level_dict["WARN"] = set_custom_handler
            handler_level_dict["ERROR"] = set_custom_handler
            handler_level_dict["CRITICAL"] = set_custom_handler
            handler_level_dict.get(handler_level_str.upper(), set_default_handler)()
            log_handler_obj.setFormatter(self.__obj_formatter)
            self.__logger_obj.addHandler(log_handler_obj)
            self.__handler_dict[handler_name] = log_handler_obj

        def del_handler():
            if handler_name in self.__handler_dict.keys():
                self.__logger_obj.removeHandler(self.__handler_dict[log_write_file])

        if log_write_file:
            handler_name = log_write_file
        else:
            handler_name = "stream"

        handle_mode_dict = dict()
        handle_mode_dict["add"] = set_handler
        handle_mode_dict["del"] = del_handler
        handle_mode_dict.get(log_mode.lower(), del_handler)()
        return self

    def debug(self, input_var):
        """
        @public: debug日志
        @param input_var: 日志内容
        @return: 无
        """
        self.__logger_obj.debug(input_var)

    def info(self, input_var):
        """
        @public: info日志
        @param input_var: 日志内容
        @return: 无
        """
        self.__logger_obj.info(input_var)

    def warn(self, input_var):
        """
        @public: warn日志
        @param input_var: 日志内容
        @return: 无
        """
        self.__logger_obj.warning(input_var)

    def error(self, input_var):
        """
        @public: error日志
        @param input_var: 日志内容
        @return: 无
        """
        self.__logger_obj.error(input_var)

    def critical(self, input_var):
        """
        @public: critical日志
        @param input_var: 日志内容
        @return: 无
        """
        self.__logger_obj.critical(input_var)




if __name__ == "__main__":
    logger = LoggerSetting()
    logger.level = "DEBUG"
    # 或者
    logger("DEBUG")

    logger.set_log_format("full")
    logger.logger_handler("add","log.txt")
    # logger.logger_handler("add", "D:\\xx.log")
    logger.error("12345上山打老虎")
    logger.debug("saddsa")
    # logger.logger_handler("del", "D:\\xx.log")
    # logger.info("45678")
