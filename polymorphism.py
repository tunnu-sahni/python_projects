# x = "hello world"

# print(len(x))


# print(x)



# mytuple = ("apple", "banana", "chery")

# print(len(mytuple))



thisdict = {
    "brand": "ford",
    "model": "mustand",
    "year": 1964
}

print(thisdict)




# class polymorphism


class car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive")


class boat:
    def __init__(self,brand , model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail")

class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")


car1 = car("ford", "mustand")
       #create a car object

boat1 = boat("ibiza", "touring 20")
#create a boat object

plane1 = plane("boeing", "747") 
         #create a plane object
for x in (car1, boat1, plane1):
    x.move()