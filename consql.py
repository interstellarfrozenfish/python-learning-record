import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="Addfish",
    password="Mm13116247415",
    database="test"
)
print("Connection successful!")
conn.close()