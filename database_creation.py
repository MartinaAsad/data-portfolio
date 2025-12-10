import mysql.connector as msql
from mysql.connector import Error
from config import DatabaseConfig

config = DatabaseConfig()
try:
    conn = msql.connect(host=config.get_host, user=config.get_user,  
                        password=config.get_password)
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE arg_airports")
        print("arg_airports database is created")
except Error as e:
    print("Error while connecting to MySQL", e)