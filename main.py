from PasswordGenerator import PasswordGenerator, proceed
from PasswordDataBase import Password_Manager, Register_Login




def main():
    
    while True:
        print("Password Manager")
        print("")
        print("1.Create your password.")
        print("2.Password Manager.")
        print("3.Quit the application")
        print("")

        try:
            user_choice = int(input("Please choose one of the options: "))

        except ValueError:
            print("")
            print("Please enter numbers not characters.")
            print("")
            proceed()
            continue

        if user_choice == 1:
            print("")
            print("Create your password!")
            proceed()
            PasswordGenerator.Generator_Manager()

        elif user_choice == 2:
            proceed()
            print("Password Manager!")
            user_id = Register_Login()
            if user_id is not None:
                password_manager = Password_Manager(user_id=user_id)
            proceed()
        
        elif user_choice == 3:
            print("")
            print("Thanks for using this application! Bye!")
            print("")
            break

        else:
            print("\nWrong option. Please enter a number in range of 1-6")
            print("")
            proceed()
            continue




program_start = main()



    
