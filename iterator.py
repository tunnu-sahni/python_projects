# mytuple = ("apple", "banana", "cherry", "grapes")

# myit = iter(mytuple)


# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


mytuple = ("tunnu","sahni", "raipur")
myit = iter(mytuple)


print(next(myit))
print(next(myit))
print(next(myit))  



mystr = "tunnu"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



#looping through an iterator



mytuple = ("banana", "cherry", "haidar")

for x in mytuple:

    print(x)




mystr = "banana"

for x in mystr:
    print(x)



mystr = "tunnu"
for x in mystr:
    print(x)




#create an iterator


class mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    

    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))




#stopiteration


class mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 200:
            x = self.a
            self.a += 1
            return x
        
        else:
            raise StopIteration
        
myclass = mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)