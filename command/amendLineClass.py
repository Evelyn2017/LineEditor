#!usr/bin/python
#-*- coding: utf-8 -*-
from command import commandFather
import os
####################插入行子类########################################
class insertLine(commandFather.commandFather):
    def __init__(self, path, lineNo, content):
        self.path = path
        self.lineNo = lineNo
        self.content = content

    def execute(self):
        print("\t----- Inserting into  file <{}> -----".format(self.path))
        with open(self.path, mode = 'r') as lineFile:
            line = lineFile.readlines()
            line.insert(self.lineNo, self.content+'\n')
            lineFile.close()
        with open(self.path, mode = 'w')as inslineFile:
            for i in range(len(line)):
                inslineFile.write(line[i])
                print("\t%d: " % i, line[i])


    def undo(self):
        print("\t----- Undoing command insert -----")
        with open(self.path, mode = 'r') as lineFile:
            line = lineFile.readlines()
            #line.delete(self.lineNo, self.content)
            del line[self.lineNo]
            lineFile.close()
        with open(self.path, mode = 'w')as inslineFile:
            for i in range(len(line)):
                inslineFile.write(line[i])
                print("\t%d: " % i, line[i])

    def redo(self):
        print("\t----- Redoing command insert -----")
        with open(self.path, mode = 'r') as lineFile:
            line = lineFile.readlines()
            line.insert(self.lineNo, self.content + '\n')
            lineFile.close()
        with open(self.path, mode = 'w')as inslineFile:
            for i in range(len(line)):
                inslineFile.write(line[i])
                print("\t%d: " %i, line[i])

######################删除行子类#######################################
class deleteLine(commandFather.commandFather):
    def __init__(self, path, lineNo):
        self.path = path
        self.lineNo = lineNo
        self.__line = open(self.path).readlines()[self.lineNo]#存储被删除的那行
#按照行号删除操作
    def execute(self):
        print("\t----- Deleting line of  file <{}> -----".format(self.path))
        with open(self.path) as file:
            line = file.readlines()
            del line[self.lineNo]
            file.close()
        with open(self.path, 'w')as delfile:
            for i in range(len(line)):
                delfile.write(line[i])
                print("\t%d: " % i, line[i])

    def undo(self):
        print("\t----- Undoing command delete -----")
        with open(self.path, mode = 'r') as lineFile:
            line = lineFile.readlines()
            line.insert(self.lineNo, self.__line)
            lineFile.close()
        with open(self.path, mode = 'w')as inslineFile:
            for i in range(len(line)):
                inslineFile.write(line[i])
                print("\t%d: " % i, line[i])

    def redo(self):
        print("\t----- Redoing command delete -----")
        with open(self.path) as file:
            line = file.readlines()
            del line[self.lineNo]
            file.close()
        with open(self.path, 'w')as delfile:
            for i in range(len(line)):
                delfile.write(line[i])
                print("\t%d: " % i, line[i])

#####################修改行子类########################################
class editLine(commandFather.commandFather):
    def __init__(self,path, line_no, edit_content):
        self.path = path
        self.lineNo = line_no
        self.editContent = edit_content
        self.__line = open(self.path).readlines()[self.lineNo]
#按照行号编辑操作
    def execute(self):
        print("\t----- Editing into  file <{}> -----".format(self.path))
        with open(self.path) as file:
            line = file.readlines()
            line[self.lineNo] = self.editContent
            file.close()
        with open(self.path, 'w')as editfile:
            for i in range(len(line)):
                editfile.write(line[i])
                print("\t%d: " % i, line[i])

    def undo(self):
        print("\t----- Undong command edit -----")
        with open(self.path) as file:
            line = file.readlines()
            line[self.lineNo] = self.__line
            file.close()
        with open(self.path, 'w')as editfile:
            for i in range(len(line)):
                editfile.write(line[i])
                print("\t%d: " % i, line[i])

    def redo(self):
        print("\t----- Redoing ----")
        with open(self.path) as file:
            line = file.readlines()
            line[self.lineNo] = self.editContent
            file.close()
        with open(self.path, 'w')as editfile:
            for i in range(len(line)):
                editfile.write(line[i])
                print("\t%d: " % i, line[i])
