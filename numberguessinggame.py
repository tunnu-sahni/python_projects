import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("welcome the number guess game:")

    print("main ne ek number socha  hai 1 se 100 ke beech usse guess karo:")

    while True:
        guess = int(input("apna guess dalo!"))

        attempts +=1

        if guess < secret_number:
            print("thoda aur bada try karo!")

        elif guess > secret_number:
            print("thoda aur chhota try karo!")

        else:
            print("f sahi jawab tumne {attempts} attempts me guess kar liya.")
            break

number_guessing_game()