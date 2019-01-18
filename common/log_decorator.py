import functools
from log.logger_setting import logger
Logger = logger
def log_something(text,index = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            #print(text)
            Logger.info((text + str(args[index])))
            try:
                result = func(*args,**kwargs)
                Logger.error(text + str(args[index]) + "：成功")
                return result
            except:
                Logger.error(text + str(args[index]) + "：失败")

        return wrapper
    return decorator
def log_op(text,index = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            #print(text)
            Logger.info((text + str(args[index])))
            try:
                result = func(*args,**kwargs)
                #Logger.error(text + str(args[index]) + "：成功")
                if result == 0:
                    Logger.error(text + str(args[index]) + ":未找到内容")
                return result
            except:
                Logger.error(text + str(args[index]) + "：失败")
        return wrapper
    return decorator
def log_result(text,index = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            #print(text)
            Logger.info((text + str(args[index])))
            try:
                result = func(*args,**kwargs)
                if result:
                    Logger.info("成功:" + text + str(args[index]))
                else:
                    Logger.error("失败：" + text + str(args[index]))
                return result
            except:
                Logger.error("图片不存在：" + str(args[index]))
        return wrapper
    return decorator
def log_testnow(text,index = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            #print(text)
            Logger.info((text + str(args[index][0])))
            #Logger.error(text + str(args[index][0]) + "：成功")
            return func(*args,**kwargs)
        return wrapper
    return decorator
def log_one(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            #print(text)
            Logger.info((text ))
            try:
                result = func(*args,**kwargs)
                Logger.info(text + "：成功")
                return result
            except:
                Logger.error(text + "：失败")
            return func(*args,**kwargs)
        return wrapper
    return decorator
