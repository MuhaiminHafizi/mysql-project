import mysql.connector
import hashlib
continuation = True


def check():
    ans = input("Do you wish to try again?(y/n): ")

    if ans == "y":
        continuation = True
        return continuation

    else:
        print("Shutting down program")
        continuation = False
        return continuation

while continuation == True:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "Muhaimin",
        password = "123choice",
        database =  "userdata_pass"
    )
    print(mydb)
    mycursor = mydb.cursor()

    print("Hey welcome to a special program")
    veri = input("Do you wish to register or login?(r/l): ")

    if veri == "l":
        print("Please enter your username and password accordingly")

        user_int = str(input("Please type in your existing username: "))
        pass_int = str(input("Please type in your existing password: "))

        sql = str("SELECT username FROM userdata_pass_table WHERE username = '" + user_int + "'")

        mycursor.execute(sql)

        myresult = mycursor.fetchone()

        if str(myresult) == "('" + user_int + "',)":
            print("Username matched!")
            sql2 = str("SELECT password FROM userdata_pass_table WHERE password = '" + pass_int + "'")

            mycursor.execute(sql2)

            myresult2 = mycursor.fetchone()

            if str(myresult2) == "('" + pass_int + "',)":
                print("Password matched!")
                print("Congrats you're logged in!")
                continuation = False

            else:
                print("It seems like the password doesn't matched ")
                continuation = False

                a = check()
                if a == True:
                    continuation = True
        else:
            print("It seems like the username doesn't exist ")
            continuation = False

            b = check()
            if b == True:
                continuation = True

    elif veri == "r":
        new_user = input("Please input your new username: ")
        new_pass = input("Please input your new password: ")

        h = hashlib.new("SHA256")
        h.update(new_user.encode())
        hnuc1 = h.hexdigest()

        sql5 = "SELECT username FROM userdata_pass_table WHERE username = '" + hnuc1 + "'"

        mycursor.execute(sql5)

        myresult3 = mycursor.fetchone()

        try:
            if myresult3[0] == hnuc1:
                print("This username is being used by somebody else. Please choose a different username")

            else:
                print("hashing does not match")
                print(hnuc2, hnuc1)

        except:
            sql4 = "INSERT INTO userdata_pass_table (username,password) VALUES (%s,%s)"

            h = hashlib.new("SHA256")
            h.update(new_user.encode())
            hash_new_user = h.hexdigest()

            h = hashlib.new("SHA256")
            h.update(new_pass.encode())
            hash_new_pass = h.hexdigest()

            input_ = (hash_new_user, hash_new_pass)

            mycursor.execute(sql4, input_)

            mydb.commit()

            print("Congratulation! You're registered in the database.")











