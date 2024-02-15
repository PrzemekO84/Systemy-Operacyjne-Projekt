import random
import string
import os
import pyperclip
import msvcrt
#Importy potrzebnych bibliotek

letters = string.ascii_letters
digits = string.digits
chars = string.punctuation

def proceed():
    print("")
    print("Press any key to proceed.")
    msvcrt.getch()
    os.system('cls' if os.name == 'nt' else 'clear')

    
    # print("")
    # print("Press any key to proceed.")
    # input()
    # os.system("cls")

#Klasa PasswordGenerator
class PasswordGenerator:

    def __init__(self):
        print("Password Generator.\n")

    #Funkcja wyboru typu hasła
    def Password_Type(self):
        while True:
            print("Do you want to create your own password structure or do you just want to create a random password?")
            print("")
            print("1. Yes, I want to create my own password structure (Choosing characters).")
            print("2. No, I just want a random password.")
            print("")
            try:
                user_password_option = int(input("Please choose option 1 or 2: "))
            except ValueError:
                print("")
                print("Please enter a valid number.")
                proceed()
                continue

            if user_password_option in [1, 2]:
                proceed()
                return user_password_option
            else:
                print("")
                print("Incorrect option. Please choose between 1 or 2.\n")
                proceed()
                continue

    #Funkcja pytajaca o długość hasła
    def Password_Length(self):
        while True:
            try:
                print("")
                password_length = int(input("How long do you want your password to be? (minimum 8, maximum 20) : "))
            except ValueError:
                print("")
                print("Please use numbers not characters.")
                proceed()
                continue

            if 8 <= password_length <= 20:
                print("")
                print("Password length = " + str(password_length) + " characters.")
                proceed()
                return password_length
            else:
                print("")
                print("Password length must be between 8 and 20.")
                proceed()

    #Tworzenie hasła ze wskasówkami od użytkownika
    def User_Password(self, password_length):

        #options = ["yes", "y", "no", "n"]
        chars_option = ""
        password = []

        print("")
        print("Please choose what chars do you want in your password.\n")
        
        #Dodanie liter
        while True:
            user_choice_letters = input("Do you want letters in your password? (Yes/No) or (y/n) : ")
            user_choice_letters.lower()

            if user_choice_letters == "yes" or user_choice_letters == "y":
                chars_option += letters
                print("")
                print("Letters added to password")
                #proceed()
                break
            elif user_choice_letters == "no" or user_choice_letters == "n":
                print("")
                print("No letters in password!")
                proceed()
                break
            else:
                print("")
                print("Wrong option. Please choose correct answer, (Yes/No) or (y/n)")
                proceed()
                continue

        #Dodanie cyfr
        while True:
            print("")
            user_choice_digits = input("Do you want digits in your password ? (Yes/No) or (y/n) : ")
            user_choice_digits.lower()

            if user_choice_digits == "yes" or user_choice_digits == "y":
                chars_option += digits
                print("")
                print("Digits added to password!")
                #proceed()
                break
            elif user_choice_digits == "no" or user_choice_digits == "n":
                print("")
                print("No digits in password!")
                proceed()
                break
            else:
                print("")
                print("Wrong option. Please choose correct answer, (Yes/No) or (y/n)")
                proceed()
                continue

        #Dodanie znaków
        while True:
            print("")
            user_choice_chars = input("Do you want chars in your password ? (Yes/No) or (y/n) : ")
            user_choice_chars.lower()

            if user_choice_chars == "yes" or user_choice_chars == "y":
                chars_option += chars
                print("")
                print("Chars added to password!")
                #proceed()
                break
            elif user_choice_chars == "no" or user_choice_chars == "n":
                print("")
                print("No chars in password!")
                proceed()
                break
            else:
                print("")
                print("Wrong option. Please choose correct answer, (Yes/No) or (y/n)")
                proceed()
                continue

        #Tworzenie hasła
        for x in range(password_length):
            x = random.choice(chars_option)
            password.append(x)

        
        string_password = "".join(password)
        print("")
        print("\033[94mYour password is:\033[0m " + string_password)

        #Zapis hasła do schowka
        while True:
            print("")
            clipboard = input("Do you want to save the password to clipboard? (Yes/No) or (y/n) : ")
            clipboard.lower()

            if clipboard == "yes" or clipboard == "y":
                pyperclip.copy(str(string_password))
                print("")
                print("Your password has been saved!")
                proceed()
                break
            elif clipboard == 'no' or clipboard == "n":
                print("")
                print("Password not saved in clipboard.")
                proceed()
                break
            else:
                print("")
                print("Please choose correct answer (Yes/No) or (y/n) : ")
                proceed()
                continue
    
    #Tworzenie hasła bez wskazówek użytkownika
    def Random_Password(self, password_length):
        print("")
        print("Creating random password!")
        print("")

        chars_group = letters + digits + chars
        password = []

        #Tworzenie hasła
        for random_char in range(password_length):

            random_char = random.choice(chars_group)

            password.append(random_char)

        string_password = "".join(password)
        print("\033[94mYour password is:\033[0m " + string_password)

        #Zapis hasła do schowka
        while True:
            print("")
            clipboard = input("Do you want to save the password to clipboard? (Yes/No) or (y/n) : ")
            clipboard.lower()

            if clipboard == "yes" or clipboard == "y":
                pyperclip.copy(str(string_password))
                print("")
                print("Your password has been saved!")
                proceed()
                break
            elif clipboard == 'no' or clipboard == "n":
                print("")
                print("Password not saved in clipboard.")
                proceed()
                break
            else:
                print("")
                print("Please choose correct answer (Yes/No) or (y/n) : ")
                proceed()
                continue

    #Główna funkcja do obsługi generatora haseł
    def Generator_Manager():
        password_generator = PasswordGenerator()
        password_type = password_generator.Password_Type()
        password_length = password_generator.Password_Length()

        if password_type == 1:
            password_generator.User_Password(password_length)

        elif password_type == 2:
            password_generator.Random_Password(password_length)           


#if __name__ == "__main__":
    # password_generator = PasswordGenerator()
    # user_choice_password_type = password_generator.Password_Type()
    # user_choice_password_length = password_generator.Password_Length()


    # if user_choice_password_type == 1:
    #     password_generator.User_Password(user_choice_password_length)

    # elif user_choice_password_type == 2:
    #     password_generator.Random_Password(user_choice_password_length) 


    
       





    

    

    

