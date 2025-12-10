import mysql.connector as msql
from mysql.connector import Error
from config import DatabaseConfig
import pandas as pd

config = DatabaseConfig()
info = pd.read_csv('aeropuertos_arg_limpio.csv')
try:
    conn = msql.connect(host=config.get_host, user=config.get_user,  
                        password=config.get_password)
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("USE arg_airports;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS flights;')
        print('Creating table....')
        cursor.execute("""
            CREATE TABLE flights (
                clasificacion_vuelo   VARCHAR(10),
                clase_vuelo           VARCHAR(10),
                aerolinea             VARCHAR(40),
                origen_provincia      VARCHAR(40),
                pais_origen           VARCHAR(40),
                destino_provincia     VARCHAR(40),
                pais_destino          VARCHAR(40),
                continente_destino    VARCHAR(40),
                cant_pasajeros        INT,
                cant_asientos         INT,
                cant_vuelos           INT,
                aeropuerto_origen     VARCHAR(40),
                aeropuerto_destino    VARCHAR(40),
                id_flights            INT NOT NULL AUTO_INCREMENT PRIMARY KEY
            );
        """)

        print("flights table is created....")
        
        print("flight table table is created....")
        for i,row in info.iterrows():
            sql = "INSERT INTO arg_airports.flights VALUES (%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)