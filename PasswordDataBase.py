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
            print("Requirements: Password length 5-20 characters")
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
                proceed()

            elif len(username) > 20 or len(username) < 4:
                print("")
                print("Incorrect username! (Requirements: Username length 4-20 characters)")
                proceed()

            elif len(password) > 20 or len(password) < 5:
                print()
                print("Incorrect password (Requirements: Password length 6-20 characters)")
                proceed()

            else:
                user_insert_values = (username, password)
                mycursor.execute("INSERT INTO users (username, user_password) VALUES (%s, %s)", user_insert_values)
                print("")
                print("You registered your account!")
                print()
                print("Now login into your account.")
                proceed()
                project_db.commit()
                continue

        elif user_option == 2:
            print("")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

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
            update_password = Update_Password(user_id)
        
        elif user_option == 4:
            break

        else:
            print("Wrong option please choose number between 1 or 4") 
            continue  

         

def Show_List(user_id):
    print("")
    check_query = "SELECT * FROM passwords where user_id = %s"
    mycursor.execute(check_query, (user_id,))
    # result = mycursor.fetchall()

    # if not result:
    #     print("You don't have any passwords saved!")
    #     proceed()
    #     return 0
    
    print("Name of page: ")
    print("")
    count = 1

    for x in mycursor:
        print(f"{count}." f"{x[2]}")
        print("")
        count += 1

    user_website_choice = input("Please type the name of webiste to show password: ")
    print("")

    if len(user_website_choice) <= 0:
        print("This field cannot be empty!")
        proceed()
        return 0

     

    check_query = "SELECT * FROM passwords WHERE page = %s AND user_id = %s"
    mycursor.execute(check_query, (user_website_choice, user_id))
    result = mycursor.fetchone()

    #lower_result = result[2].lower()
    #print(lower_result)
    

    if result is None:
        print("Page doesn't exists")
        proceed()
    
    else:
        print("Name of page: " f"{result[2]}\n")
        print("Login: " f"{result[3]}")
        print("Password: " f"{result[4]}")
        proceed()
        return 0
        
   

def Adding_Password(user_id):
    print("Adding password!")
    print("")
    page = input("Please enter the name of page: ")
    login = input("Please enter the login: ")
    password = input("Please enter the password: ")

    check_query = "SELECT COUNT(*) FROM passwords WHERE user_id = %s and page = %s"
    mycursor.execute(check_query, (user_id, page))
    result = mycursor.fetchone()

    if result is not None:
        print("")
        print("Name of page already exists in database. Please delete it or update the password!")
        proceed()
    
    elif len(page) <= 0 or len(page) > 20:
        print("Name of your page must be between 1-20 characters!")
        proceed()
    
    elif len(login) <= 0 or len(login) > 20:
        print("Login must be between 1-20 characters!")
        proceed()

    elif len(password) <= 0 or len(password) > 30:
        print("Password length must be between 1-30 characters!")
        proceed()

    else:
        print("")
        print("Password added successfully")
        mycursor.execute("INSERT INTO passwords (user_id, page, login, password) Values(%s, %s, %s, %s)", (user_id, page, login, password))
        proceed()
        project_db.commit()
    

def Update_Password(user_id):
    print("")
    print("Updating password!")
    print("")

    check_query = "SELECT * FROM passwords where user_id = %s"
    mycursor.execute(check_query, (user_id,))
    result = mycursor.fetchall()


    if not result:
        print("You don't have any passwords saved!")
        proceed()
        return 0

    print("Name of page: ")
    print("")
    count = 1

    for x in result:
        print(f"{count}." f"{x[2]}")
        print("")
        count += 1

    update_choice = input("Please type the name of the page that you want to change the password: ")

    check_query = "SELECT * FROM passwords WHERE page = %s AND user_id = %s"
    mycursor.execute(check_query, (update_choice, user_id))
    result = mycursor.fetchone()

    if result is None:
        print("You didn't saved password for this page!")

    elif len(update_choice) <= 0:
        print("This field cannot be empty!")

    else:
        print("siema")

    

    

    
password_manager = Password_Manager(user_id=Register_Login())



#TODO napraw adding password zawsze pokazuje ze istnieje strona, jak drugi raz probujesz wejsc w showlist i update to wywala czemu ??????????????  xDddD
#dodaj delte popraw caly interfejs i bedzie git