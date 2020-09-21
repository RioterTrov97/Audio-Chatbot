import sqlite3

def db_insert(fn,mn,ln,e,pw,ad,n):
    try:
        sqliteConnection = sqlite3.connect('chatbot.db')
        cursor = sqliteConnection.cursor()
        #print("db_insert: Successfully Connected to SQLite")
        
        sqlite_insert_query = '''INSERT INTO user (user_fname, user_mname, user_lname, email, password, address, nickname) VALUES
                                    (?,?,?,?,?,?,?);'''
        
        cursor.execute(sqlite_insert_query, (fn,mn,ln,e,pw,ad,n))
        sqliteConnection.commit()
        #print("SQLite user created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while inserting into sqlite table. Please provide all the required details.", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("sqlite connection is closed")

def db_nickname(n,uid, email):
    try:
        import main
        sqliteConnection = sqlite3.connect('chatbot.db')
        cursor = sqliteConnection.cursor()
        #print("db_nickname: Successfully Connected to SQLite")
        
        sqlite_insert_query = '''UPDATE user SET nickname = ? WHERE user_id = ?'''
        
        cursor.execute(sqlite_insert_query, (n, uid))
        sqliteConnection.commit()
        #print("SQLite log: nickname updated")

        sqlite_select_query = "SELECT * FROM user WHERE email = ?"
        cursor.execute(sqlite_select_query, (email,))
        records = cursor.fetchall()
        for row in records:
            main.uid = int(row[0])
            main.email = str(row[4])
            main.person_obj.name = str(row[7])

        cursor.close()

    except sqlite3.Error as error:
        print("Error while updating nickname in sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("sqlite connection is closed")

def db_createdb():
    try:
        sqliteConnection = sqlite3.connect('chatbot.db')
        cursor = sqliteConnection.cursor()
        #print("db_create: Successfully Connected to SQLite")
        
        sqlite_insert_query = '''CREATE TABLE IF NOT EXISTS user (	"user_id"	INTEGER,	"user_fname"	TEXT NOT NULL,
        "user_mname"	TEXT,	"user_lname"	TEXT NOT NULL,	"email"	TEXT NOT NULL UNIQUE,	"password"	TEXT NOT NULL,
        "address"	TEXT,	"nickname"	TEXT,	PRIMARY KEY("user_id" AUTOINCREMENT));'''
        
        cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        cursor.close()
        create_admin()
    except sqlite3.Error as error:
        print("Error while creating a sqlite database and a table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("sqlite connection is closed")

def create_admin():
    try:
        sqliteConnection = sqlite3.connect('chatbot.db')
        cursor = sqliteConnection.cursor()
        #print("db_admin: Successfully Connected to SQLite")
        
        sqlite_select_query = "SELECT * FROM user"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        if (len(records)) < 1:
            db_insert("root","root","root","root","root","root","")
            #print("SQLite database created and populated with default details.")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite entry for default records", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("sqlite connection is closed")

def check_user_data(email, password):
    try:
        import main
        sqliteConnection = sqlite3.connect('chatbot.db')
        cursor = sqliteConnection.cursor()
        #print("check_user_data: Successfully Connected to SQLite")

        sqlite_select_query = "SELECT * FROM user WHERE email = ? AND password = ?"
        cursor.execute(sqlite_select_query, (email,password))
        records = cursor.fetchall()
        for row in records:
            main.uid = int(row[0])
            main.email = str(row[4])
            name = str(row[7])
            name = default_name(name)

        if (len(records) > 0):
            print("You are successfully logged in")
            return True
        else:
            return False
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("The Sqlite connection is closed")

def check_users_data(email, fname, lname):
    try:
        import main
        sqliteConnection = sqlite3.connect('chatbot.db')
        cursor = sqliteConnection.cursor()
        #print("check_user_data: Successfully Connected to SQLite")
        email, fname, lname = str(email), str(fname), str(lname)
        sqlite_select_query = "SELECT * FROM user WHERE email = ? AND user_fname = ? AND user_lname = ?"
        cursor.execute(sqlite_select_query, (email, fname, lname))
        records = cursor.fetchall()
        for row in records:
            main.uid = int(row[0])

        if (len(records) > 0):
            return True
        else:
            return False
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("The Sqlite connection is closed")

def db_password(password):
    try:
        import main
        sqliteConnection = sqlite3.connect('chatbot.db')
        cursor = sqliteConnection.cursor()
        #print("db_nickname: Successfully Connected to SQLite")
        
        sqlite_insert_query = '''UPDATE user SET password = ? WHERE user_id = ?'''
        
        cursor.execute(sqlite_insert_query, (password, main.uid))
        sqliteConnection.commit()
        #print("SQLite log: nickname updated")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while updating nickname in sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("sqlite connection is closed")

def get_user_data(email, password):
    try:
        import main
        sqliteConnection = sqlite3.connect('chatbot.db')
        cursor = sqliteConnection.cursor()
        #print("check_user_data: Successfully Connected to SQLite")

        sqlite_select_query = "SELECT * FROM user WHERE email = ? AND password = ?"
        cursor.execute(sqlite_select_query, (email,password))
        records = cursor.fetchall()
        for row in records:
            main.uid = int(row[0])
            main.email = str(row[4])
            name = str(row[7])
            name = default_name(name)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("The Sqlite connection is closed")

def check_default_data(email, password):
    try:
        import main
        sqliteConnection = sqlite3.connect('chatbot.db')
        cursor = sqliteConnection.cursor()
        #print("check_user_data: Successfully Connected to SQLite")

        sqlite_select_query = "SELECT * FROM user WHERE email = ? AND password = ?"
        cursor.execute(sqlite_select_query, (email,password))
        records = cursor.fetchall()
        for row in records:
            main.uid = int(row[0])
            main.email = str(row[4])
            name = str(row[7])
            name = default_name(name)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("The Sqlite connection is closed")

def default_name(name):
    import main
    if (name == ""):
        main.person_obj.name = 'Master'
    else:
        main.person_obj.name = name

def register():
    fn = input ("Enter your first name: ")
    mn = input ("Enter your middle name(optional): ")
    ln = input ("Enter your last name: ")
    e = input ("Enter your email: ")
    pw = str(pw_check(e))
    #print("reg: This is password: " + pw)
    ad = input ("Enter your address(optional): ")
    n = input ("Enter your nickname(optional): ")
    db_insert(fn,mn,ln,e,pw,ad,n)
    join()

def pw_check(e):
    if (e != ""):
        pw1 = input ("Enter your password: ")
        pw2 = input ("Confirm your password: ")
        if (pw1 == pw2):
            pas = str(pw1)
            #print("check: This is password: " + pas)
            return (pas)
        else:
            print("Sorry your password does not match")
            return (pw_check(e))
    else:
        print("Email is empty")
        register()
        
    
def login():
    import main
    e = input ("Enter your email: ")
    pw = input ("Enter your password: ")
    log = check_user_data(e, pw)
    if log:
        import queue
        q = queue.Queue()
        main.initial_greeting(q)
    else:
        print("Your email or password is incorrect.")
        error()

def db_error():
    try:
            value = int(input("Enter 1 to login again or 2 to main menu."))
            if (value == 1):
                login()
            elif (value == 2):
                join()
            else:
                print("Sorry wrong number")
                db_error()
    except Exception:
            print("Sorry wrong number")
            db_error()

def join():
    try:
        print(" --------------------------------------------------------------------")
        print(" |                     ***Chatbot Cutie pie!***                     |")
        print(" |                                                                  |")
        print(" |                   ***Commandline version***                      |")
        print(" |                                                                  |")
        print(" |          -->Please login if you are an existing user.            |")
        print(" |                                                                  |")
        print(" |          -->If you are a new user, please register.              |")
        print(" |                                                                  |")
        print(" --------------------------------------------------------------------")
        print("")
        val = int(input ("Do you want to login or register? (1 for login/ 2 for register)"))
        if (val == 1):
            login()
        elif (val == 2):
            register()
        else:
            import os
            clear = lambda: os.system('cls')
            clear()

            print("\n***Sorry you selected wrong number***\n")
            join()
    except Exception:
        import os
        os.system('cls')
        import speaker
        speaker.offline_output('Sorry, the service is down. Please connect to the internet and try again.')
        join()

def start():
    db_createdb()
    join()

if __name__ == '__main__':
    print("Program starting........")
    start()