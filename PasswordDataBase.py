import mysql.connector as mysql
from PasswordGenerator import proceed

#Łączenie się z MySQL
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
    print("Could not connect to Project DataBase.")    

#Tworzenie cursora
mycursor = project_db.cursor(buffered=True)


#Funkcja do rejestracji lub logowania użytkownika
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
        
        #Rejestracja użytkownika
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
            
        #Logowanie użytkownika
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

        #Wyjście z programu 
        elif user_option == 3:
            print("")
            print("See you soon!")
            return None

        else:
            print("Wrong option choose number 1 or 2")
            proceed()
            continue

#Menu dla menadżera haseł
def Password_Manager(user_id):
    while True:
        print("")
        print("1.Show list of your passwords.")
        print("2.Add password.")
        print("3.Change password")
        print("4.Change login")
        print("5.Delete password")
        print("6.Exit")

        try:
            print("")
            user_option = int(input("Please choose an option : "))

        except ValueError:
            print("Please choose number option. Do not use characters.")
            proceed()
            continue

        #Lista haseł w bazie danych
        if user_option == 1:
            print("")
            print("Show list of passwords!")
            show_list = Show_List(user_id)  
        
        #Dodawanie hasła do bazy danych
        elif user_option == 2:
            print("")
            print("Add the password!")
            adding_password = Adding_Password(user_id)

        #Zmiana hasła dla strony
        elif user_option == 3:
            print("")
            print("Change the password!")
            update_password = Update_Password(user_id)
        
        #Zmiana użytkownika dla strony
        elif user_option == 4:
            print("")
            print("Change the login!")
            update_login = Update_Login(user_id)

        #Usuwanie strony z hasłem i loginem
        elif user_option == 5:
            print("")
            print(f"Delete the Password!")
            delete_password = Delete(user_id)

        #Wyjście z programu
        elif user_option == 6:
            print("")
            print("Thanks for using this application. Bye!")
            break

        else:
            print("")
            print("Wrong option please choose number between 1 or 6")
            proceed() 
            continue  
       
#Funkcja do wyświetlenia haseł w bazie danych
def Show_List(user_id):
    print("")
    #Sprawdzenie czy użytkownik posiada jakiekolwiek hasła
    check_query = "SELECT * FROM passwords where user_id = %s"
    mycursor.execute(check_query, (user_id,))
    result = mycursor.fetchall()

    if not result:
        print("You don't have any passwords saved!")
        proceed()
        return 0
    
    #Wypisanie haseł
    print("Name of page: ")
    print("")
    count = 1

    for x in result:
        print(f"{count}." f"{x[2]}")
        print("")
        count += 1

    user_website_choice = input("Please type the name of webiste to show password: ")
    print("")

    if len(user_website_choice) <= 0:
        print("This field cannot be empty!")
        proceed()
        return 0

    #Sprawdzenie czy wybrana strona przez użytkownika istnieje 
    check_query = "SELECT * FROM passwords WHERE page = %s AND user_id = %s"
    mycursor.execute(check_query, (user_website_choice, user_id))
    result = mycursor.fetchone()

    #lower_result = result[2].lower()
    #print(lower_result)
    
    if result is None:
        print("Page doesn't exists")
        proceed()
    
    #Wyświetlenie wyników
    else:
        print("")
        print("\033[94mName of page:\033[0m " f"{result[2]}\n")  # Blue color
        print("\033[92mLogin:\033[0m " f"{result[3]}")          # Green color
        print("\033[91mPassword:\033[0m " f"{result[4]}")      # Red color
        proceed()
        return 0
        
#Funkcja do dodawania haseł
def Adding_Password(user_id):
    print("")
    #Wprowadzenie danych
    page = input("Please enter the name of page: ")
    login = input("Please enter the login: ")
    password = input("Please enter the password: ")

    #Sprawdzenie czy podana strona nie została już wcześniej wprowadzona
    check_query = "SELECT COUNT(*) FROM passwords WHERE user_id = %s and page = %s"
    mycursor.execute(check_query, (user_id, page))
    result = mycursor.fetchone()

    if result[0] > 0:
        print("")
        print("Name of the page already exists in database. Please delete it or update the password!")
        proceed()
    
    elif len(page) <= 0 or len(page) > 20:
        print("")
        print("Name of your page must be between 1-20 characters!")
        proceed()
    
    elif len(login) <= 0 or len(login) > 20:
        print("")
        print("Login must be between 1-20 characters!")
        proceed()

    elif len(password) <= 0 or len(password) > 30:
        print("")
        print("Password length must be between 1-30 characters!")
        proceed()

    #Wprowadzenie strony do razem z loginem i hasłem do bazy danych
    else:
        print("")
        print("Password added successfully")
        mycursor.execute("INSERT INTO passwords (user_id, page, login, password) Values(%s, %s, %s, %s)", (user_id, page, login, password))
        proceed()
        project_db.commit()
    

#Akutalizacja hasła
def Update_Password(user_id):
    print("")
    #Sprawdzenie czy użytkownik posiada już jakieś strony z hasłami w bazie danych
    check_query = "SELECT * FROM passwords where user_id = %s"
    mycursor.execute(check_query, (user_id,))
    result = mycursor.fetchall()


    if not result:
        print("You don't have any passwords saved!")
        proceed()
        return 0

    #Wyświetlenie stron
    print("Name of pages: ")
    print("")
    count = 1

    for x in result:
        print(f"{count}." f"{x[2]}")
        print("")
        count += 1

    update_choice = input("Please type the name of the page that you want to change the password: ")

    #Sprawdzenie czy podana strona przez użytkownika istnieje
    check_query = "SELECT * FROM passwords WHERE page = %s AND user_id = %s"
    mycursor.execute(check_query, (update_choice, user_id))
    result = mycursor.fetchone()

    if len(update_choice) <= 0:
        print("")
        print("This field cannot be empty!")
        proceed()

    elif result is None:
        print("")
        print("You didn't saved password for this page!")
        proceed()

    else:
        print("")
        new_password = input("Please type new password: ")

        if len(new_password) > 30 or len(new_password) <= 0:
            print("")
            print("Password must be between 1-30 characters!")
            proceed()
            return 0

        #Akutalizacja hasła w odpowiedni wiersz
        check_query = "UPDATE passwords SET password = %s WHERE user_id = %s and page = %s"
        mycursor.execute(check_query, (new_password, user_id, update_choice))

        project_db.commit()
        print("")
        print("Password updated successfully!")

        proceed()


def Update_Login(user_id):
    print("")
    #Sprawdzenie czy użytkownik posiada już jakieś strony z hasłami w bazie danych
    check_query = "SELECT * FROM passwords where user_id = %s"
    mycursor.execute(check_query, (user_id,))
    result = mycursor.fetchall()

    if not result:
        print("You didn't saved any password yet!")
        proceed()
        return 0
    
    #Wyświetlenie stron
    print("Name of pages: ")
    print("")

    count = 1

    for x in result:
        print(f"{count}." f"{x[2]}")
        print("")
        count += 1

    update_choice = input("Please type the name of the page that you want to change the login: ")

    #Sprawdzenie czy podana strona przez użytkownika istnieje
    check_query = "SELECT * FROM passwords WHERE user_id = %s and page = %s"
    mycursor.execute(check_query, (user_id, update_choice))
    result = mycursor.fetchone()

    if len(update_choice) <= 0:
        print("")
        print("This field cannot be empty!")
        proceed()

    elif result is None:
        print("")
        print("You didn't saved password for this page!")
        proceed()

    else:
        print("")
        new_login = input("Please type new login: ")   

        if len(new_login) > 30 or len(new_login) <= 0:
            print("")
            print("Login must be between 1-30 characters!")
            proceed()
            return 0

        #Akutalizacja loginu w odpowiedni wiersz
        check_query = "UPDATE passwords SET login = %s WHERE user_id = %s AND page = %s"
        mycursor.execute(check_query, (new_login, user_id, update_choice))

        project_db.commit()
        print("")
        print("Login updated successfully!")

        proceed()


def Delete(user_id):
    print("")
    #Sprawdzenie czy użytkownik posiada już jakieś strony z hasłami w bazie danych
    check_query = "SELECT * FROM passwords where user_id = %s"
    mycursor.execute(check_query, (user_id,))
    result = mycursor.fetchall()

    if not result:
        print("You didn't saved any password yet!")
        proceed()
        return 0
    
    #Wyświetlenie stron
    print("Name of pages: ")
    print("")

    count = 1

    for x in result:
        print(f"{count}." f"{x[2]}")
        print("")
        count += 1

    delete_choice = input("Please type the name of the page that you want to delete: ")

    #Sprawdzenie czy podana strona przez użytkownika istnieje
    check_query = "SELECT * FROM passwords WHERE user_id = %s and page = %s"
    mycursor.execute(check_query, (user_id, delete_choice))
    result = mycursor.fetchone()

    if len(delete_choice) <= 0:
        print("")
        print("This field cannot be empty!")
        proceed()

    elif result is None:
        print("")
        print("You didn't saved password for this page!")
        proceed()
  

    else:   
        #Usunięcie strony/loginu/hasła z odpowiedniego wiersza
        check_query = "DELETE FROM passwords WHERE user_id = %s AND page = %s"
        mycursor.execute(check_query, (user_id, delete_choice))

        project_db.commit()
        print("")
        print("Password deleted successfully!")

        proceed()

        

if __name__ == "__main__":
    password_manager = Password_Manager(user_id=Register_Login())
    

