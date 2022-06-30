# @Author : 杨佳杰
# @Time   : 2022/6/30 14:59
# @File   : 7-将日志输出到文件.py
import logging

logging.basicConfig(level=logging.INFO,
                    filename='log.txt',
                    filemode='w',
                    encoding='utf8',
                    format='%(asctime)s-'
                           '%(pathname)s'
                           '%(filename)s[line:%(lineno)d]-'
                           '%(process)d-'
                           '%(levelname)s(%(levelno)s): %(message)s')

logging.debug('这是 logging debug message')
logging.info('这是 logging info message')
logging.warning('这是 logging warning message')
logging.error('这是 logging error message')
logging.critical('这是 logging critiaal message')
