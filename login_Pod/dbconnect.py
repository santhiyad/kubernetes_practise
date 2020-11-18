import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        #host='mysql',
        user='root',
        passwd='Sant@wip08'
        )

except Error as e:
    print("error while connecting to mysql" , e)


# create loginForm database if not exist
def database_creation():
    try:
        mycursor = mydb.cursor()
        mycursor.execute('show databases')
        mydatabases = mycursor.fetchall()

        database_create = True
        for database in mydatabases:
            print(database)
            student_db = "{0}".format(database[0])
            print(student_db, flush=True)

            if student_db == "loginForm":
                print("loginForm Database already created !", flush=True)
                database_create = False
                break
        if database_create:
            mycursor.execute("CREATE DATABASE loginForm")
            print("loginForm Database created !", flush=True)
    except Error as e:
        print("Error while creating loginForm database", e)


# create users table if not exist
def table_creation():
    try:
        mydb = mysql.connector.connect(
           # host="mysql",
            user="root",
            passwd="Sant@wip08"
        )

        mycursor = mydb.cursor()
        mycursor.execute("USE loginForm")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        users_table_create = True
        for table in tables:
            users_table = "{0}".format(table[0])
            print( users_table , flush=True)

            if users_table == "users":
                print("users table already created !", flush=True)
                users_table_create = False
                break
        if users_table_create:
            mycursor.execute(
                "CREATE TABLE users ( name VARCHAR(25), passwd VARCHAR(25))")
            print("users table  created !", flush=True)

    except Error as e:
        print("Error while creating table ", e)


# user_entry
def submit(name,passwd):
    try:

        mydb = mysql.connector.connect(
            #host='mysql',
            user='root',
            passwd='Sant@wip08'
            )
        print("inside submit")
        mycursor = mydb.cursor()
        mycursor.execute('USE loginForm')
        print("Using users table")
        sql = "INSERT into users values(%s,%s)"
        val = (name,passwd)
        mycursor.execute(sql,val)
        print("creating --->")
        mydb.commit()
        #mydb.close()
        return 'Login Success'
    except Error as e :
        print("error while user entry", e)



