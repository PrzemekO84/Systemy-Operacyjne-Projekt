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
            print("Requirements: Username length 4-20 characters")
            print("Requirements: Password length 8-20 characters")
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

            elif len(username) > 20 or len(username) < 4:
                print("")
                print("Incorrect username! (Requirements: Username length 4-20 characters)")
                proceed()

            elif len(password) > 20 or len(password) < 8:
                print()
                print("Incorrect password (Requirements: Password length 8-20 characters)")
                proceed()

            else:
                user_insert_values = (username, password)
                mycursor.execute("INSERT INTO users (username, user_password) VALUES (%s, %s)", user_insert_values)
                print("")
                print("You registered your account!")
                print("Now login into your account.")
                proceed()
                project_db.commit()
                continue

        elif user_option == 2:
            username = input("Please enter your username: ")
            password = input("Please enter your password:  ")

            check_query = "SELECT * FROM users WHERE username = %s and user_password = %s"
            mycursor.execute(check_query, (username, password))
            result = mycursor.fetchone()

            if result is None:
                print("")
                print("User doesn't exists.")
                proceed()
            
            else:
                print("")
                print("Welcome in your password manager.")
                proceed()
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
            show_list = Show_List(user_id)  
        
        elif user_option == 2:
            print("Add password")
            adding_password = Adding_Password(user_id)

        elif user_option == 3:
            print("Change password")
        
        elif user_option == 4:
            break

        else:
            print("Wrong option please choose number between 1 or 4") 
            continue  

         

def Show_List(user_id):
    print("")
    check_query = "SELECT * FROM passwords where user_id = %s"
    mycursor.execute(check_query, (user_id,))
    
    for x in mycursor:
        print("Name of Website: " f"{x[2]}")
        print("")

    user_website_choice = input("Please type the name of webiste to show password: ")

    check_query = "SELECT * FROM passwords WHERE page = %s and user_id = %s"
    mycursor.execute(check_query, (user_website_choice, user_id))
    result = mycursor.fetchone()
    

    if result is None:
        print("Page doesn't exists")
    
    else:
        for x in result:
            print(x)



    
        

        

    

def Adding_Password(user_id):
    print("")
    page = input("Please enter the name of page: ")
    login = input("Please enter the login: ")
    password = input("Please enter the password: ")
    mycursor.execute("INSERT INTO passwords (user_id, page, login, password) Values(%s, %s, %s, %s)", (user_id, page, login, password))
    
    project_db.commit()
    


password_manager = Password_Manager(user_id=Register_Login())


#TODO mozna zalozyc puste konto bez znakow XD, jesli nie uzytkownik nie ma zadnych hasel to wyswietl wiadomosc
#lower() name of page ? sprawdzaj insert czy taka strona juz istnieje, czasami jak dodajesz hasla na nowym koncie to 
# user_id sie nie dodaje do tabeli password XD czemu ?