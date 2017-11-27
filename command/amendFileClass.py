#!usr/bin/python
#-*- coding:utf-8 -*-
import os
from command import viewFile
from shutil import *
from command import commandFather
import time
veribose = True
##########################打开/创建文件子类###########################################################
class CreateFile(commandFather.commandFather):
    def __init__(self, path, txt=""):
        self.path, self.txt = path, txt

    def execute(self):
        if veribose:
            if os.path.exists(self.path):
                print("\t----- file <{}> already exists -----".format(self.path))
            else:
                print("\t----- Creating file <{}> ----- ".format(self.path))
                time.sleep(2)
                with open(self.path, mode = 'w', encoding = 'utf-8') as out_file:
                    out_file.write(self.txt)
                print("\t----- Created file <{}> ----- ".format(self.path))

        file_created = viewFile.ReadFile(self.path)
        file_created.execute()

############################重命名文件子类#########################################################
class RenameFile(commandFather.commandFather):
    def __init__(self, path_src, path_dest):
        self.src, self.dest, = path_src, path_dest

    def execute(self):
        if(veribose):
            print("\t----- Renaming <{}> back to <{}> -----".format(self.src, self.dest))
            time.sleep(2)
        os.rename(self.src, self.dest)
        print("Rename successed! ")

    def undo(self):
        if veribose:
            print("\t----- Renamed <{}> back to <{}> -----".format(self.dest, self.src))
        os.rename(self.dest, self.src)

    def redo(self):
        print("\t----- Renamed <{}> back to <{}> -----".format(self.src, self.dest))
        os.rename(self.src, self.dest)

#######################删除文件子类#################################################################
class deleteFile(commandFather.commandFather):
    def __init__(self, path):
        self.path = path

    def execute(self):
        if os.path.exists(self.path):
            print("\t----- Deleting file <{}> -----".format(self.path))
            time.sleep(2)
            copyfile(self.path, self.path + '.copy')
            os.remove(self.path)
            print("\t-----delete file <{}> successed -----".format(self.path))

        else:
            print("\t----- file <{}> doesn't exist! -----\n"
                  "\t----- can't perform the command -----".format(self.path))

    def undo(self):
        os.rename(self.path + '.copy', self.path)
        print("\t----- undo: recover file <{}> successed! -----".format(self.path))

###########################复制文件子类#############################################################
class copyFile(commandFather.commandFather):
    def __init__(self, path):
        self.path = path

    def execute(self):
        print("\t----- Copying file <{}> -----".format(self.path))
        time.sleep(2)
        copyfile(self.path, self.path + '.copy')
        print("\t-----Copy file <{}> successed -----".format(self.path))

    def undo(self):
        delete_file(self.path + '.copy')
        print("\t----- undo: deleted copy file <{}> successed! -----".format(self.path + '.copy'))

def delete_file(path):
    os.remove(path)