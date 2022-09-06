import mysql.connector as ms

con = ms.connect(host="localhost", user="root", passwd="true@1234star", database="bank")
if con.is_connected():
    print("Connection Established")
else:
    print("Some error occurred !!!!")

mycursor = con.cursor()

t1 = "Create table account (AccNo int(14) Not Null auto_increment, Name varchar(15),DOB date not null , OpeningBal float Default 0,Primary Key(AccNo))"
mycursor.execute(t1)
t2 = "Create table amount (AccNo int(14) Not Null auto_increment,Name varchar(15) not null, Balance float Default 0, Primary Key(AccNo))"
mycursor.execute(t2)
t3 = "Create Table login (Username varchar(15) Primary key, password varchar(18) Not Null)"
mycursor.execute(t3)
t4 = "Create Table alogin(AUsername varchar(15) Primary Key, Apassword varchar(18) Not Null)"
mycursor.execute(t4)

