# @Author : 杨佳杰
# @Time   : 2022/6/30 15:05
# @File   : 8-即输出到文件又输出到控制台.py
import logging

# 第一步，创建一个 logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关
# 总开关设定了整个程序中日志文件的下限值,创建新的handler时的level若低于总开关,则按照总开关实施
# 若高于总开关,则按自身设置的level实施

# 第二步，创建一个 handler，用于写入日志文件
log_file = 'log.txt'
fh = logging.FileHandler(log_file, mode='a',encoding='utf8')
fh.setLevel(logging.DEBUG)

# 第三步，再创建一个 handler，用于输出到控制台
sh = logging.StreamHandler()
sh.setLevel(logging.WARNING)

# 第四步，定义 handler 的输出格式
formatter = logging.Formatter('%(asctime)s-'
                              '%(pathname)s'
                              '%(filename)s[line:%(lineno)d]-'
                              '%(process)d-'
                              '%(levelname)s(%(levelno)s): %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

# 第五步，将 logger 添加到 handler 里面
logger.addHandler(fh)
logger.addHandler(sh)

# 日志
logger.debug('这是 logger debug message')
logger.info('这是 logger info message')
logger.warning('这是 logger warning message')
logger.error('这是 logger error message')
logger.critical('这是 logger critical message')
