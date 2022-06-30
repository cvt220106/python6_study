# @Author : 杨佳杰
# @Time   : 2022/6/30 14:47
# @File   : 6-学习python自带的日志框架.py
import logging

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s-%(process)d-%(filename)s[line:%(lineno)d]-%(levelname)s: %(message)s')

logging.debug('这是 logging debug message')
logging.info('这是 logging info message')
logging.warning('这是 logging warning message')
logging.error('这是 logging error message')
logging.critical('这是 logging critiaal message')