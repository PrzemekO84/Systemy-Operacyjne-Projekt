import random
import string
import os
import pyperclip

letters = string.ascii_letters
digits = string.digits
chars = string.punctuation

def proceed():
    print("")
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
                print("")
                password_length = int(input("How long do you want your password to be? (minimum 8, maximum 20) : "))
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
        
        while True:
            user_choice_letters = input("Do you want letters in your password? (Yes/No) or (y/n) : ")
            user_choice_letters.lower()

            if user_choice_letters == "yes" or user_choice_letters == "y":
                chars_option += letters
                print("Letters added to password")
                proceed()
                break
            elif user_choice_letters == "no" or user_choice_letters == "n":
                print("No letters in password!")
                proceed()
                break
            else:
                print("")
                print("Wrong option. Please choose correct answer, (Yes/No) or (y/n)")
                proceed()
                continue
                
                
        
        
        while True:
            user_choice_digits = input("Do you want digits in your password ? (Yes/No) or (y/n) : ")
            user_choice_digits.lower()

            if user_choice_digits == "yes" or user_choice_digits == "y":
                chars_option += digits
                print("Digits added to password!")
                proceed()
                break
            elif user_choice_digits == "no" or user_choice_digits == "n":
                print("No digits in password!")
                proceed()
                break
            else:
                print("")
                print("Wrong option. Please choose correct answer, (Yes/No) or (y/n)")
                proceed()
                continue

        
        while True:
            user_choice_chars = input("Do you want chars in your password ? (Yes/No) or (y/n) : ")
            user_choice_chars.lower()

            if user_choice_chars == "yes" or user_choice_chars == "y":
                chars_option += chars
                print("Chars added to password!")
                proceed()
                break
            elif user_choice_chars == "no" or user_choice_chars == "n":
                print("No chars in password!")
                proceed()
                break
            else:
                print("")
                print("Wrong option. Please choose correct answer, (Yes/No) or (y/n)")
                proceed()
                continue

        for x in range(password_length):
            x = random.choice(chars_option)
            password.append(x)

        
        string_password = "".join(password)
        print("Your password is " + string_password)

        while True:
            clipboard = input("Do you want to save the password to clipboard? (Yes/No) or (y/n) : ")
            clipboard.lower()

            if clipboard == "yes" or clipboard == "y":
                pyperclip.copy(str(string_password))
                print("")
                print("Your password has been saved!")
                break
            elif clipboard == 'no' or clipboard == "n":
                print("")
                print("Password not saved in clipboard.")
                break
            else:
                print("")
                print("Please choose correct answer (Yes/No) or (y/n) : ")
                proceed()
                continue
    
    def Random_Password(self, password_length):
        print("")
        print("Creating random password!")
        print("")

        chars_group = letters + digits + chars
        password = []

        for random_char in range(password_length):

            random_char = random.choice(chars_group)

            password.append(random_char)

        string_password = "".join(password)
        print("Your password is " + string_password)

    
        while True:
            clipboard = input("Do you want to save the password to clipboard? (Yes/No) or (y/n) : ")
            clipboard.lower()

            if clipboard == "yes" or clipboard == "y":
                pyperclip.copy(str(string_password))
                print("")
                print("Your password has been saved!")
                break
            elif clipboard == 'no' or clipboard == "n":
                print("")
                print("Password not saved in clipboard.")
                break
            else:
                print("")
                print("Please choose correct answer (Yes/No) or (y/n) : ")
                proceed()
                continue



if __name__ == "__main__":
    password_generator = PasswordGenerator()
    user_choice_password_type = password_generator.Password_Type()
    user_choice_password_length = password_generator.Password_Length()


    if user_choice_password_type == 1:
        password_generator.User_Password(user_choice_password_length)

    elif user_choice_password_type == 2:
        password_generator.Random_Password(user_choice_password_length) 


    
       





    

    

    

