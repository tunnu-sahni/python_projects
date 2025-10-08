# Generate Password

import random
import string

def generate_password(length=12):
    # characters use in password

    characters =string.ascii_letters + string.digits + string.punctuation

    # generate random password
    password =''.join(random.choice(characters)) 
    for _ in range(length):
     return password
        
def main():
    print("password generator:")

    # ask user for password length
    length =int(input("enter password length:"))

    password = generate_password(length)
    print("your generated password is:",password)

if __name__ == "__main__":
 main()





# generate password

import random
import string

def generate_password(length= 20):
   # character use in password
   character = string.ascii_letters + string.digits + string.punctuation

   # generate random password

   password = ''.join(random.choice(character))

   for _ in range(length):
      return password
   
def main():
   print("password generator: ")

   length = int(input("enter password length:"))

   password = generate_password(length)
   print("your generated password is:",password)

if __name__ =="__main__":
   main()