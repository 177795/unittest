from loguru import logger


# 输出日志到txt文件，三参数，1、文件名称   2、日志格式    3、日志级别,只会输入比设置的更高级别的日志，一般都会填写INFO
logger.add('logs.txt', format="{time} {level} {message}", level='WARNING')
# debug日志
logger.debug('debug日志    10')
# 一般日志
logger.info("info日志    20")
# 成功日志
logger.success('susses日志   30')
# 警告日志
logger.warning('warning日志   40')
# 报错日志
logger.error('error日志   50')




