import mysql.connector

def db(nama, nomor):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_db"
    )

    mycursor = mydb.cursor()

    sql = "SELECT FROM data WHERE Nama = (%s)"
    val = (nama)

    if(nama == mycursor.execute(sql,val)):
        print('success')

# !Cek database
# mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)

#? Insert database
# mycursor = mydb.cursor()

# sql = "INSERT INTO data(Nama, id) VALUES (%s, %s)"
# Nama = input()
# iid = int(input())

# val = (Nama, iid)
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")