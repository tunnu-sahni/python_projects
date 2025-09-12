# try:
#     print(x)
# except:
#     print("an exception occured")


#many exception

# try:
#     print(x)
# except NameError:
#     print("variable x is not defined")

# except:
#     print("something else went wrong")


# try:
#     print("hello")

# except:
#     print("something went wrong")

# else:
#     print("nothing went wrong")


# try:
#     print(x)
# except:
#     print("something went wrong")
# finally:
#     print("the try except is finished")



# close object and clean resourses

try:
    f = open("demofile.txt")
    try:
        f.write("lorum ipsum")
    except:
        print("something went wrong when writing to the file")

    finally:
        f.close()
except:
    print("something went wrong when opening the file") 



# raise an exception

# x = -1 

# if x < 0:
#   raise Exception("sorry, no numbers below zero")

# print(x)


x = "hello"

if not type(x) is int:
    raise TypeError("only integers are allowed")

print(x)