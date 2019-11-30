# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 17:48
# @Author  : Mr Li
import logging
lg=logging.getLogger(__name__)
formater=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
lg.setLevel(logging.DEBUG)

f=logging.FileHandler('log.txt')
f.setLevel(logging.DEBUG)
f.setFormatter(formater)

h=logging.StreamHandler()
h.setLevel(logging.DEBUG)
h.setFormatter(formater)

lg.addHandler(f)
lg.addHandler(h)


lg.debug('dddddd')
lg.warning('warrrrrr')
lg.error('errrr')
lg.info('infffff')

'''
StreamHandler：logging.StreamHandler；日志输出到流，可以是sys.stderr，sys.stdout或者文件
FileHandler：logging.FileHandler；日志输出到文件
BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式
RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚
TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件
SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets
DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets
SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址
SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog
NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志
MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer
HTTPHandler：logging.handlers.HTTPHandler；通过"GET"或者"POST"远程输出到HTTP服务器
'''
