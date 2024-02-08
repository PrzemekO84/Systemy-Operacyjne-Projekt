import os
#from ShowFolderFilers import wyswietl_foldery, nawiguj_po_folderach
from PasswordGenerator import PasswordGenerator, proceed



def main():
    
    while True:
        print("File Manager")
        print("1. Show folder/files")
        print("2. Show list of passwords")
        print("3. Create a new strong password for the site")
        print("4. Encrypt a file")
        print("5. Decrypt a file")
        print("6. Quit the application")

        try:
            user_choice = int(input("Please choose one of the options:"))
        except ValueError:
            print("\nPlease enter a number not words")
            print("")
            proceed()
            continue

        if user_choice == 1:
            print("\nwyswietl Folderki ;d")
            print("")
            proceed()

        elif user_choice == 2:
            print("\nShow list of passwords ")
            print("")
            proceed()

        elif user_choice == 3:
            print("\nCreate a new strong password for the site")
            print("")
            
            password_generator = PasswordGenerator()
            user_choice_password_type = password_generator.Password_Type()
            user_choice_password_length = password_generator.Password_Length()


            if user_choice_password_type == 1:
                password_generator.User_Password(user_choice_password_length)

            elif user_choice_password_type == 2:
                password_generator.Random_Password(user_choice_password_length)

            print("")
            proceed()

        elif user_choice == 4:
            print("\nEncrypt a file")
            print("")
            proceed()

        elif user_choice == 5:
            print("\nDecrypt a file")
            print("")
            proceed()

        elif user_choice == 6:
            print("\nQuit the appliaction")
            print("")
            break

        else:
            print("\nWrong option. Please enter a number in range of 1-6")
            print("")
            proceed()
            continue




program_start = main()



    
