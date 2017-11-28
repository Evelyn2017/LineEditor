#!usr/bin/python
# -*- coding:utf-8 -*-
from client import user
def editline(path):
    print("\n\t++++++++++++++++++++++++++++++++++++++++++ view mode ++++++++++++++++++++++++++++++++++++++++++\n")
    print("\ti: ----insert into file <{}>\t".format(path))
    print("\td: ---- delete line of file <{}>\t".format(path))
    print("\te: ---- edit line of file <{}>\t".format(path))
    print("\texit: ---- exit edit line mode")

    op = input()
    return op

def cut():
    cmdbuffer = []   #记录命令历史
    while(1):
        print("\n\n\t------------------------------------------ main mode ------------------------------------------\n"
              "\top: ---- open/create file\t"
              "de: ---- delete file\t"
              "cp: ---- copy file\t"
              "rn: ---- rename file\n"
              )
        command = input()
        command_ls = command.split(' ')
        #cmdbuffer.append(command_ls)
        objbuffer = []
        redobuffer = []
        if(command_ls[0] in 'Qq'):
            exit(0)
        if(command_ls[0] == 'op'):#进入编辑模式
            actop = user.createclient(command_ls[1])
            actop.run(command_ls[0])
            cmdbuffer.append(command_ls)
            while(1):
                command = editline(actop.filename)
                command_ls = command.split(' ')
                if(command_ls[0] == 'exit'):#退出编辑模式
                    break
                if(command_ls[0] == 'i'):
                    cmdbuffer.append(command_ls)
                    actins= user.insertlineclient(actop.filename, int(command_ls[1]), command_ls[2])
                    actins.run(command_ls[0])
                    objbuffer.append(user.insertlineclient(actop.filename, int(command_ls[1]), command_ls[2]))
                    #print(str(act[index].action))
                elif(command_ls[0] == 'd'):
                    cmdbuffer.append(command_ls)
                    actdeline = user.deletelineclient(actop.filename, int(command_ls[1]))
                    actdeline.run(command_ls[0])
                    objbuffer.append(user.deletelineclient(actop.filename, int(command_ls[1])))
                elif(command_ls[0] == 'e'):
                    cmdbuffer.append(command_ls)
                    actedit = user.editlineclient(actop.filename, int(command_ls[1]), command_ls[2])
                    actedit.run(command_ls[0])
                    objbuffer.append(user.editlineclient(actop.filename, int(command_ls[1]), command_ls[2]))

                if (command_ls[0] == 'undo'):
                    print(objbuffer)
                    objbuffer[-1].action.actionundo()
                    redobuffer.append(objbuffer[-1])
                    del objbuffer[-1]
                if (command_ls[0] == 'redo'):
                    redobuffer[-1].action.actionredo()
                    del redobuffer[-1]

        if(command_ls[0] == 'de'):
            cmdbuffer.append(command_ls)
            actde = user.deletefileclient(command_ls[1])
            actde.run(command_ls[0])
            objbuffer.append(user.deletefileclient(command_ls[1]))
        if(command_ls[0] == 'rn'):
            actrn = user.renamefileclient(command_ls[1], command_ls[2])
            actrn.run(command_ls[0])
        if(command_ls[0] == 'cp'):
            actcp = user.copyfileclient(command_ls[1])
            actcp.run(command_ls[0])

        if(command_ls[0] == 'undo'):
            print(objbuffer)
            objbuffer[-1].action.actionundo()
            redobuffer.append(objbuffer[-1])
            del objbuffer[-1]

        if(command_ls[0] == 'redo'):
            redobuffer[-1].action.actionredo()
            del redobuffer[-1]

        if(command_ls[0] == 'history'):
            print(cmdbuffer)
cut()
