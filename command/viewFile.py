#!/bin/usr/python
# -*- coding : utf-8 -*-
from command import commandFather
veribose = True

#########################查看文件子类#############################################################
class ReadFile(commandFather.commandFather):
    def __init__(self, path):
        self.path = path

    def execute(self):
        if veribose:
            print("\t----- Reading file <{}> -----".format(self.path))
        with open(self.path, mode = 'r', encoding = 'utf-8') as inFile:
            #inFile = open(self.path, 'r')
            #for (num, value) in enumerate(inFile):
             #   print(num, "->", value)
            print(inFile.read(),'\n')
