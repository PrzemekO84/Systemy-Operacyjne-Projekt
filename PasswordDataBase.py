import mysql.connector as mysql

try:
    db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#password'
    )
    print("Successfully connected to MySQL server.")
except Exception as e:
    print(e)
    print("Could not connect to MySQL server.")

try:
    Project = mysql.connect(
        host = "localhost",
        user = "root",
        password = "#password",
        database = "PasswordManager"
    )
    print("Successfully connected to Procjet DataBase.")
except Exception as e:
    print(e)
    print("Could not connect to Project DataBase. ")

