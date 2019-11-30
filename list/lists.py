# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 9:37
# @Author  : Mr Li
spam = ['cat', 'bat', 'rat', 'elephant']
s=str(','.join(spam))
print(s)
import os
import xlwt
import time

package='com.eebbk.askhomework'

def getcpu():
    try:
        cmd=("adb shell \"top -n 1 -b | grep %s\""%package)
        content=os.popen(cmd)
        line=content.readlines()
        print(line)
        if package in line[0]:
            cpu=line[0].split()[8]
            return cpu
    except:
        pass
def getmem():
    try:
        cmd=("adb shell \"dumpsys meminfo | grep %s\""%package)
        content=os.popen(cmd)
        line=content.readlines()
        print(line)
        if package in line[0]:
            mem=line[0].split()[0].replace("K:","")
            return mem
    except:
        pass

def times():
    try:
        times=time.strftime('%Y-%m-%d-%X')
        return times
    except:
        pass


wb=xlwt.Workbook()
sheet1=wb.add_sheet('cpu',cell_overwrite_ok=True)
sheet1.write(0,0,'time')
sheet1.write(0,1,'mem')
sheet1.write(0,2,'cpu')
row=1
while True:
    t=times()
    m=getmem()
    c=getcpu()
    sheet1.write(row,0,t)
    sheet1.write(row,1,m)
    sheet1.write(row,2,c)
    time.sleep(2)
    row+=1
    wb.save('cpu&mem.csv'.encode())









#long running
#do something other
# end = time.process_time()
# print(end)

# print(s.split(1))
# while True:
#     print('enter the name spece over:')
#     name=input()
#     if name=='':
#         break
#     creatname+=[name]
# print('catnames:')
# for name in creatname:
#     print (name)

# from datetime import *
# td=datetime.now()
# print (td)
# t=time.strftime('%Y-%m-%d %H:%M:%S')
# print(t)