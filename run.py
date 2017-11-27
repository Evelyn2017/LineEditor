#!usr/bin/python
#-*- coding: utf-8 -*-

import os
from command import amendLineClass
from command import amendFileClass
from command import viewFile
from command import commandFather

while(1):
    print("----- a.打开/创建文件    b.删除文件    c.查看目录 -----")
    commands = []
    command = input().split(' ')
    print(command)
    if(command[0] == 'a'):
        commands.append(command[0])
        filea = amendFileClass.CreateFile(command[1])
        filea.execute()
    if(command[0]=='b'):
        commands.append(command[0])
        fileb = amendFileClass.deleteFile(command[1])
        fileb.execute()
    if(command =='undo'):
        commands.append(command)

        print(commands)
    if(input()=='stop'):
        break