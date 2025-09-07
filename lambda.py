# x = lambda a : a + 10
# print(x(5))


# x = lambda a : a - 10
# print(x(5))


# x = lambda a : a * 10
# print(x(3))


# x = lambda a , b : a * b
# print(x(5 , 6))



# x = lambda a , b, c : a + b + c
# print(x(4 , 6, 7)) 



# x = lambda a , b ,c : a + b * c
# print(x(4 , 5 ,9))





def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



def myfunc(n):
    return lambda a : a * n

mytriple = myfunc(3)

print(mytriple(11))





def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler =myfunc(3)

print(mydoubler(11))
print(mytriple(11))

