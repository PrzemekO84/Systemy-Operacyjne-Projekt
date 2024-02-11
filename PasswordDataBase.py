import mysql.connector as mysql
from PasswordGenerator import proceed

#Proba polaczenia sie z baza danych MySQL
try:
    db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'siemaeniu'
    )
    print("Successfully connected to MySQL server.")
except Exception as e:
    print(e)
    print("Could not connect to MySQL server.")

#Laczenie z baza danych PasswordManager
try:
    project_db = mysql.connect(
        host = "localhost",
        user = "root",
        password = "siemaeniu",
        database = "PasswordManager"
    )
    print("Successfully connected to Procjet DataBase.")
except Exception as e:
    print(e)
    print("Could not connect to Project DataBase. ")


mycursor = project_db.cursor()

def Register_Login():
    while True:
        print("")
        print("1.Register account.")
        print("2.Login to your account.")
        print("3.Exit")

        try:
            print("")
            user_option = int(input("Please choose options : "))

        except ValueError:
            print("")
            print("Please choose number option. Do not use characters.")
            proceed()
            continue

        if user_option == 1:
            print("")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            
            check_query = "SELECT COUNT(*) FROM users WHERE username =%s"
            mycursor.execute(check_query, (username,))
            result = mycursor.fetchone()

            if result[0] > 0:
                print("")
                print("Username already exists!")
                print("")
                print("Please choose different username.")

            elif len(username) > 20:
                print("")
                print("Your username is to long! (Maximum username length is 20 characters)")

            else:
                user_insert_values = (username, password)
                mycursor.execute("INSERT INTO users (username, user_password) VALUES (%s, %s)", user_insert_values)
                project_db.commit()
                break

        elif user_option == 2:
            username = input("Please enter your username: ")
            password = input("Please enter your password:  ")

            check_query = "SELECT * FROM users WHERE username = %s and user_password = %s"
            mycursor.execute(check_query, (username, password))
            result = mycursor.fetchone()

            if result is None:
                print("")
                print("User doesn't exists.")
            
            else:
                print("")
                print("Welcome in your password manager.")
                user_id = result[0]
                return user_id
            
        elif user_option == 3:
            print("")
            print("See you soon!")
            break

        else:
            print("Wrong option choose number 1 or 2")
            proceed()
            continue


def Password_Manager(user_id):
    while True:
        print("")
        print("1.Show list of your passwords.")
        print("2.Add password.")
        print("3.Change password")
        print("4.Exit")

        try:
            print("")
            user_option = int(input("Please choose option : "))

        except ValueError:
            print("Please choose number option. Do not use characters.")
            continue

        if user_option == 1:
            print("Show list of passwords")
            show_password = Show_Passwords(user_id)
            show_password
            
        
        elif user_option == 2:
            print("Add password")
            adding_password = Adding_Password(user_id)
            adding_password

        elif user_option == 3:
            print("Change password")

        else:
            print("Wrong option please choose number between 1 or 4") 
            continue  

         

def Show_Passwords(user_id):
    print("")
    check_query = "SELECT * FROM passwords where user_id = %s"
    mycursor.execute(check_query, (user_id,))
    
    for x in mycursor:
        print(x)

    

def Adding_Password(user_id):
    print("")
    page = input("Please enter the name of page: ")
    login = input("Please enter the login: ")
    password = input("Please enter the password: ")
    mycursor.execute("INSERT INTO passwords (user_id, page, login, password) Values(%s, %s, %s, %s)", (user_id, page, login, password))
    
    project_db.commit()
    






register_login = Register_Login()
password_manager = Password_Manager(register_login)


