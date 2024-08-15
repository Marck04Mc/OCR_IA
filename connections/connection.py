import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="lic_db"
    )
