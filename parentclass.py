class person:
    def __init__(self , fname ,lname):
        self.firstname = fname
        self.lastname  = lname

    def printname(self):
        print(self.firstname,self.lastname)

x = person("tunnu", "sahni")
x.printname()



class person:
    def __init__(self, uname, dname):
        self.uname = uname
        self.dname = dname

    def printname(self):
        print(self.uname,self.dname)

x = person("delhi", "pune")
