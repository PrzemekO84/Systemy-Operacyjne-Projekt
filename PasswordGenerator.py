import random
import string
from prograam import proceed

program = True

print("Password Generator.\n")


print("Do you want to crate your passwod or you just want random password ?\n")
print("1. Yes I want to create my password.")
print("2. No I just want a random password.")

def Password_Type():
    while True:
        try:
            user_password_option = int(input("Please choose option between 1 or 2"))
        except ValueError:
            print("Type only numbers!")
            proceed()
            continue

        if user_password_option == 1:
            return 1
        
        elif user_password_option == 2:
            return 2
        
        else:
            print("Inccorect option please choose between 1 or 2")
            continue


password_type = Password_Type()
    






while program:

    while True:
        try:
            password_length = int(input("How long do you want you password to be\n"))

            print("minimum length: 8\n")
            print("maximum length : 20")
        except ValueError:
            print("Type only numbers!")
            proceed()
            continue

        minimum = 8
        maximum = 20

        if password_length < minimum:
            print("")
            print("Your password is to short!")

        elif password_length > 20:
            print("Your password it too long!")
        
        else:
            break


        

    

    

    

