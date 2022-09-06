import mysql.connector as ms

con = ms.connect(host="localhost", user="root", passwd="true@1234star", database="bank")
if con.is_connected():
    print("Connection Established")
else:
    print("Some error occurred !!!!")


def register():
    mycursor = con.cursor()
    q = "select AUsername from alogin"
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
                    print("Dear Admin Your Username and password has been created")


if __name__ == '__main__':
    register()
