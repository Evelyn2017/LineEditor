from command import amendFileClass
from command import amendLineClass
from invoker import  invoker
from client import clientFather

class createclient(clientFather.client):
    def __init__(self, path):
        self.filename = path
        self.actioncmd = amendFileClass.CreateFile(self.filename)
        self.action = invoker.invoker(self.actioncmd)

    def run(self, cmd):
        if (cmd == 'op'):
            self.action.doaction()

class deletefileclient(clientFather.client):
    def __init__(self, path):
        self.filename = path
        self.actioncmd = amendFileClass.deleteFile(self.filename)
        self.action = invoker.invoker(self.actioncmd)

    def run(self, cmd):
        if(cmd == 'de'):
            self.action.doaction()

class renamefileclient(clientFather.client):
    def __init__(self, path1, path2):
        self.filename1 = path1
        self.filename2 = path2
        self.actioncmd = amendFileClass.RenameFile(self.filename1, self.filename2)
        self.action = invoker.invoker(self.actioncmd)

    def run(self, cmd):
        if(cmd == 'rn'):
            self.action.doaction()

class copyfileclient(clientFather.client):
    def __init__(self, path):
        self.filename = path
        self.actioncmd = amendFileClass.copyFile(self.filename)
        self.action = invoker.invoker(self.actioncmd)

    def run(self, cmd):
        if(cmd == 'cp'):
            self.action.doaction()

class insertlineclient(clientFather.client):
    def __init__(self, path, lineNo, content):
        self.path = path
        self.lineNo = lineNo
        self.content = content
        self.actioncmd = amendLineClass.insertLine(self.path, self.lineNo, self.content)
        self.action = invoker.invoker(self.actioncmd)

    def run(self, cmd):
        if (cmd == 'i'):
            self.action.doaction()

class deletelineclient(clientFather.client):
    def __init__(self, path, lineNo):
        self.path = path
        self.lineNo = lineNo
        self.actioncmd  = amendLineClass.deleteLine(self.path, self.lineNo)
        self.action = invoker.invoker(self.actioncmd)

    def run(self, cmd):
        if(cmd == 'd'):
            self.action.doaction()

class editlineclient(clientFather.client):
    def __int__(self, path, lineNo, content):
        self.path = path
        self.lineNo = lineNo
        self.content = content
        self.actioncmd = amendLineClass.editLine(self.path, self.lineNo, self.content)
        self.action = invoker.invoker(self.actioncmd)

    def run(self, cmd):
        if(cmd == 'e'):
            self.action.doaction()
