# -*- coding: utf-8 -*-

from mail import *
from decrypt import *
import os
from datetime import datetime
main_dir = r'D:\sphere_engine'
file = r'\changes_required.html'
os.path.getsize(main_dir+file)

with open('last_file_size_list.txt','r') as initial_readfile:
    initial_read_file = eval(initial_readfile.read())


file_list = ['main.py','changes_required.html','mail.py']
file_list_size = [os.path.getsize(main_dir +"/"+file_list[i]) for i in range(len(file_list))]

""" overwrite the changes"""
with open('last_file_size_list.txt','w') as readfile:
    readfile.write(str(file_list_size))

""" compare the sizes"""
detect_files = []
for i in initial_read_file:
    if i not in file_list_size:
        detect_files.append(i)
if detect_files != []:
    email_list=["mainak@capitalnumbers.com","aritra@capitalnumbers.com"]
    file_list = ['changes_required.html']
    for i in range(len(email_list)):
        mailto(email_list[i],file_list)
else:
    None
    
""" file ran successful"""

with open(r'log\notification_log.txt','a+') as readfile:
    readfile.write(str("{}: File ran successfully \n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))



