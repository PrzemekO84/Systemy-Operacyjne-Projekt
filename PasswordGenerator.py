import random
import string
import os

letters = string.ascii_letters
digits = string.digits
chars = string.punctuation

def proceed():
    print("Press any key to proceed.")
    input()
    os.system("cls")

class PasswordGenerator:

    def __init__(self):
        print("Password Generator.\n")

    def Password_Type(self):
        print("Do you want to create your password or do you just want a random password?\n")
        print("1. Yes, I want to create my password (Choosing chars).")
        print("2. No, I just want a random password.")
        print("")

        while True:
            try:
                user_password_option = int(input("Please choose option 1 or 2: "))
            except ValueError:
                print("Please enter a valid number.\n")
                proceed()
                continue

            if user_password_option in [1, 2]:
                return user_password_option
            else:
                print("Incorrect option. Please choose between 1 or 2.\n")
                proceed()
                continue

    def Password_Length(self):
        while True:
            try:
                password_length = int(input("How long do you want your password to be? (minimum 8, maximum 20)\n"))
            except ValueError:
                print("Please enter a valid number.\n")
                proceed()
                continue

            if 8 <= password_length <= 20:
                proceed()
                return password_length
            else:
                print("Password length must be between 8 and 20.")

    def User_Password(self, password_length):

        options = ["yes", "y", "no", "n"]
        chars_option = ""
        password = []

        print("")
        print("Please choose what chars do you want in your password.\n")
        user_choice_letters = input("Do you want letters in your password ? (Yes/No)")
        user_choice_letters.lower()
        while True:
            if user_choice_letters == "Yes" or user_choice_letters == "y":
                chars_option += letters
                proceed()
                break
            else:
                print("Wrong option. Please choose correct answer, (Yes/No)\n")
                proceed()
                continue
        
        user_choice_digits = input("Do you want digits in your password ? (Yes/No)")
        user_choice_digits.lower()
        while True:
            if user_choice_letters == "Yes" or user_choice_letters == "y":
                chars_option += digits
                proceed()
                break
            else:
                print("Wrong option. Please choose correct answer, (Yes/No)\n")
                proceed()
                continue

        user_choice_chars = input("Do you want chars in your password ? (Yes/No)")
        user_choice_chars.lower()
        while True:
            if user_choice_letters == "Yes" or user_choice_letters == "y":
                chars_option += chars
                proceed()
                break
            else:
                print("Wrong option. Please choose correct answer, (Yes/No)\n")
                proceed()
                continue

        for x in range(password_length):

            randomchar = random.choice(chars_option)

            password.append(randomchar)

        
        print("Your password is " + "".join(password))


        


        

    



password_generator = PasswordGenerator()
user_choice_password_type = password_generator.Password_Type()
user_choice_password_length = password_generator.Password_Length()


if user_choice_password_type == 1:
    password_length = password_generator.User_Password(user_choice_password_length)

elif user_choice_password_type == 2:
    pass

        





    

    

    

