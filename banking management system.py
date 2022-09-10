import mysql.connector as ms

con = ms.connect(host="localhost", user="root", passwd="useyourownpassword", database="banking")
if con.is_connected():
    print("Connection Established")
else:
    print("Some error occurred !!!!")

print("\tWelcome To Laksmi Chit Fund!!!\t")


# starting menu
def smenu():
    print(".........................")
    print(".........................")
    print("Options")
    print("1.For Admin")
    print("2.OldUser")
    print("3.NewUser")
    print("4.EXIT")
    c = input("Enter options(1-3): ")
    if c == "1":
        amenu()
    elif c == "2":
        login()
    elif c == "3":
        register()
    elif c == "4":
        print("Thank You for using our services")
    else:
        print("invalid Choice !!!")


# Function to display details of Users
def display():
    mycursor = con.cursor()
    acno = int(input("Enter account number of user:"))
    q = "Select * from account where AccNo=%s"
    data = (acno,)
    mycursor.execute(q, data)
    myresult = mycursor.fetchall()
    con.commit()
    print("Details of the user are as follows:")
    for x in myresult:
        print("Name :", x[1])
        print("DOB :", x[2])
        print("Opening Balance", x[3])
    amenu()


# Menu for Admin
def amenu():
    print("Options")
    print("1.Display user details")
    print("2.Remove a bank account")
    print("3.Exit")
    c = input("Enter choice (1-3) :")
    if c == "1":
        display()
    elif c == "2":
        closeac()
    elif c == "3":
        print("Thank You ADMIN for providing your services")


# Admin Login
def alogin():
    print("Options")
    print("1.Proceed to login")
    print("2.Maybe Later.....")
    c = input("Enter option(1-2):")
    if c == "1":
        mycursor = con.cursor()
        print("DEAR ADMIN PLEASE ENTER YOUR USERNAME AND PASSWORD TO GET ACCESS......")
        uname = input("Enter username:")
        passw = input("Enter your password:")
        q = "Select * from alogin where AUsername=%s And Apassword=%s"
        data = (uname, passw)
        mycursor.execute(q, data)
        myresult = mycursor.fetchone()
        if myresult is not None:
            if myresult[0] == uname and myresult[1] == passw:
                print("Login Successful......")
                print("You are being directed.......")
                amenu()
        else:
            print("Try Again")
            alogin()
    elif c == "2":
        print("You are being directed....")
        smenu()
    else:
        print("Invalid Choice")
        print("You are being directed....")
        alogin()


# Menu for New Users
def numenu():
    print(".........................")
    print(".........................")
    print("Options")
    print("1.Open New Account")
    print("2.Exit")
    c = input("Enter option(1-2):")
    if c == "1":
        openacc()
    elif c == "2":
        print("Thank you for using our services")
    else:
        print("invalid choice")


# Function for old users to get access to their bank accounts
def login():
    print("Options")
    print("1.Proceed to login")
    print("2.Maybe Later.....")
    c = input("Enter option(1-2):")
    if c == "1":
        mycursor = con.cursor()
        uname = input("Enter username:")
        passw = input("Enter your password:")
        q = "Select * from login where Username=%s And password=%s"
        data = (uname, passw)
        mycursor.execute(q, data)
        myresult = mycursor.fetchone()
        if myresult is not None:
            if myresult[0] == uname and myresult[1] == passw:
                print("Login Successful......")
                print("You are being directed.......")
                oumenu()
        else:
            print("Try Again")
            login()
    elif c == "2":
        print("You are being directed....")
        smenu()
    else:
        print("Invalid Choice")
        print("You are being directed....")
        login()


# Menu for Old Users
def oumenu():
    print(".........................")
    print(".........................")
    print("Options")
    print("1.Deposit Amount")
    print("2.Balance Enquiry")
    print("3.Withdraw Amount")
    print("4.Close Account")
    print("5.EXIT")
    c = input("Enter Option(1-5):")
    if c == "1":
        depositam()
    elif c == "2":
        balance()
    elif c == "3":
        draw()
    elif c == "4":
        closeac()
    elif c == "5":
        print("Thank You For Using Our Services")
    else:
        print("Invalid Choice")
        smenu()

# Function to create username and password for new users
def register():
    mycursor = con.cursor()
    q = "select Username from login"
    mycursor.execute(q)
    myresult = mycursor.fetchall()
    uname = input("Create a username:")
    if len(uname) == 0:
        print("Please enter a Username")
        register()
    else:
        if (uname,) in myresult:
            print("Take another username")
            register()
        else:
            passwd = ""
            while len(passwd) == 0:
                passwd = input("Please enter a password:")
            else:
                cpass = input("Confirm Password :")
                if passwd != cpass:
                    print("Passwords don't match, restart")
                    register()
                else:
                    q = f"INSERT INTO login values('{uname}','{passwd}')"
                    mycursor.execute(q)
                    con.commit()
                    print("Your Username and password has been created")
                    print("Please proceed to make your Bank Account")
                    openacc()

# Function to create account for new users
def openacc():
    mycursor = con.cursor()
    n = input("Enter your name :")
    if len(n) > 15:
        print("Name Too long....!")
        openacc()
    else:
        d = input("Enter your Date of Birth(YYYY-MM-DD):")
        obal = float(input("Enter your opening balance:"))
        q = f"INSERT INTO account(Name, DOB, OpeningBal) VALUES('{n}','{d}',{obal})"
        q2 = f"INSERT INTO amount(Name, Balance) values('{n}',{obal})"
        mycursor.execute(q)
        mycursor.execute(q2)
        q3 = "Select AccNo From account where Name = %s"
        acno = (n,)
        mycursor.execute(q3,acno)
        myresult = mycursor.fetchall()
        con.commit()
        print("Your Account has been created")
        print("Your Account Number is:",myresult[0][0])
        print("You are being directed....")
        smenu()


# Function to deposit amount
def depositam():
    acno = int(input("Enter your account number:"))
    amt = int(input("Enter amount you want to deposit:"))
    q = "SELECT Balance from amount where AccNo=%s"
    data = (acno,)
    mycursor = con.cursor()
    mycursor.execute(q, data)
    myresult = mycursor.fetchone()
    dmt = myresult[0] + amt
    q2 = "update amount set Balance = %s where AccNo = %s"
    d2 = (dmt, acno)
    mycursor.execute(q2, d2)
    con.commit()
    oumenu()

# Function to show balance of user
def balance():
    mycursor = con.cursor()
    acno = int(input("Enter your account number:"))
    q = "SELECT Balance from amount where AccNo=%s"
    data = (acno,)
    mycursor.execute(q, data)
    myresult = mycursor.fetchall()
    con.commit()
    print("Your current bank balance is:")
    for x in myresult:
        print(x[0])
    oumenu()

# Function to withdraw amount
def draw():
    mycursor = con.cursor()
    acno = int(input("Enter your account number:"))
    q = "SELECT Balance from amount where AccNo=%s"
    data = (acno,)
    mycursor.execute(q, data)
    myresult = mycursor.fetchall()
    print("Your current bank balance is:")
    for x in myresult:
        print(x[0])
    wt = float(input("Enter amount you want to withdraw:"))
    if wt > x[0]:
        print("Insufficient Balance....")
        print("Please check your balance and Try Again !!!")
        print("You are being directed...")
        draw()
    else:
        q2 = "SELECT Balance from amount where AccNo=%s"
        d2 = (acno,)
        mycursor = con.cursor()
        mycursor.execute(q2, d2)
        myresult = mycursor.fetchone()
        dmt = myresult[0] - wt
        q3 = "Update amount set Balance = %s where AccNo = %s"
        d3 = (dmt, acno)
        mycursor.execute(q3, d3)
        con.commit()
        oumenu()

# Function to close an account
def closeac():
    mycursor = con.cursor()
    q = "select Username from login"
    mycursor.execute(q)
    myresult = mycursor.fetchall()
    uname = input("Please enter your username:")
    if (uname,) in myresult:
        acno = int(input("Enter your account number to delete from bank:"))
        q1 = "DELETE from account where AccNo = %s"
        q2 = "DELETE from amount where AccNo = %s"
        q3 = "Delete from login where Username = %s"
        data = (acno,)
        data2 = (uname,)
        mycursor.execute(q1, data)
        mycursor.execute(q2, data)
        mycursor.execute(q3, data2)
        con.commit()
        print("Your account has been removed successfully !!!")
        smenu()
    else:
        print("Username Doesn't exists")
        print("Please Try Again...!")
        closeac()


if __name__ == '__main__':
    smenu()
