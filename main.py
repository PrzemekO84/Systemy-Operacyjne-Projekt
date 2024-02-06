import os
from ShowFolderFilers import wyswietl_foldery, nawiguj_po_folderach

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


def proceed():
    print("Press any key to proceed.")
    input()
    #trzeba bedzie zamienic prawdopodobnie cls na clear dla systemu linux
    os.system("cls")

program_start = main()



    
