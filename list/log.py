# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 11:02
# @Author  : Mr Li
import logging
import datetime



#DEBUG打印所有级别日志
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
logger=logging.getLogger(__name__)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
logger.error('err....')

import sys

sys.stdout.write('hello world')

print('enter name')
name=sys.stdin.readline()[:-1]
print('hi,%s'%name)

