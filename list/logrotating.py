# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 19:47
# @Author  : Mr Li
# import logging
# from logging.handlers import RotatingFileHandler
#
# lg=logging.getLogger(__name__)
# formater=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# lg.setLevel(logging.DEBUG)
#
# filehandler=RotatingFileHandler('log.txt',maxBytes=10*1024,backupCount=3)#、备份三个10kb大小的文档
# filehandler.setLevel(logging.INFO)
# filehandler.setFormatter(formater)
#
# console=logging.StreamHandler()
# console.setLevel(logging.DEBUG)
# console.setFormatter(console)
#
# lg.addHandler(filehandler)
# lg.addHandler(console)
#
# logging.info('iiiiiiii')
# logging.error('eeeeeee')
# logging.warning('wwwwwwww')
# logging.debug('dddddddd')
import logging
from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
#定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
rHandler = RotatingFileHandler("log.txt",maxBytes = 1*1024,backupCount = 3)
rHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger.addHandler(rHandler)
logger.addHandler(console)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")