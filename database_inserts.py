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
        for i,row in info.iterrows():
            sql = "INSERT INTO arg_airports.flights (clasificacion_vuelo, clase_vuelo, aerolinea, origen_provincia, pais_origen, destino_provincia, pais_destino, continente_destino, cant_pasajeros, cant_asientos, cant_vuelos, aeropuerto_origen, aeropuerto_destino) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            #print("Record inserted")
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)