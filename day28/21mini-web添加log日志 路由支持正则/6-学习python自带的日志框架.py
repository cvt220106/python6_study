# @Author : 杨佳杰
# @Time   : 2022/6/30 14:47
# @File   : 6-学习python自带的日志框架.py
import logging

# 选择的日志级别level,则输出日志时,只输出对应level及以上的日志
# %(levelno)s: 打印日志级别的数值
# %(levelname)s: 打印日志级别名称
# %(pathname)s: 打印当前执行程序的路径，其实就是 sys.argv[0]
# %(filename)s: 打印当前执行程序名
# %(funcName)s: 打印日志的当前函数
# %(lineno)d: 打印日志的当前行号
# %(asctime)s: 打印日志的时间
# %(thread)d: 打印线程ID
# %(threadName)s: 打印线程名称
# %(process)d: 打印进程ID
# %(message)s: 打印日志信息
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s-'
                           '%(pathname)s'
                           '%(filename)s[line:%(lineno)d]-'
                           '%(process)d-'
                           '%(levelname)s(%(levelno)s): %(message)s')

logging.debug('这是logging debug message')
logging.info('这是logging info message')
logging.warning('这是logging warning message')
logging.error('这是logging error message')
logging.critical('这是logging critiaal message')