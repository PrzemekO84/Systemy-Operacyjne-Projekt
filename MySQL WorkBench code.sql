#Create database PasswordManager;
use PasswordManager;
#drop table users;
#drop table passwords;
#Create table users(
    #user_id int Primary Key auto_increment,
    #username varchar(20),
    #user_password varchar(20)
#);

#Create Table passwords(
#password_id int Primary KEY auto_increment,
#user_id int,
#page varchar(20),
#login varchar(20),
#password varchar(30),
#foreign key (user_id) references users(user_id)
#);

#drop table passwords;
Select * from users;

Select * from passwords;
