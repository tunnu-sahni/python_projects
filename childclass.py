# class person:
#     def __init__(self, fname,lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname,self.lastname)

# class Student(person):
#     pass

# x = Student("mike", "olsen")
# x.printname()    




# class person:
#     def __init__(self, fname,lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class student(person):
#     pass

# x = student("tunnu", "sahni")
# x.printname()




# class person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname

#     def print(self):
#         print(self.fname,self.lname)

# class student(person):
#     def __init__(self,fname,lname):
#         person.__init__(self,fname,lname)

# x = student("mike","olsen")
# x.printname()


#use the super function


# class person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
#         def printname(self):
#             print(self.firstname, self.lastname)

# class student(person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
# x = student("tunnu", "sahni")
# x.printname()




class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        def printname(self):
            print(self.firstname, self.lastname)

class student(person):
    def __init__(self,fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = student("tunnu", "sahni")
print(x.graduationyear) 