import pandas as pd


df = pd.read_csv('aeropuertos_arg.csv')

'''['clasificacion_vuelo', 'clase_vuelo', 'aerolinea', 'aero_origen',
       'origen_localidad', 'origen_provincia', 'pais_origen', 'aero_destino',
       'destino_localidad', 'destino_provincia', 'pais_destino',
       'continente_destino', 'cant_pasajeros', 'cant_asientos', 'cant_vuelos']      '''

#drop unnecessary columns
df = df.drop(columns=['indice_tiempo', 'origen_continente', 'origen_aeropuerto', 'destino_aeropuerto'])

#change names of columns
columns_rename = {
    'origen_oaci': 'aero_origen',
    'destino_oaci': 'aero_destino',
    'origen_pais': 'pais_origen',
    'destino_pais': 'pais_destino',
     'destino_continente': 'continente_destino',
     'pasajeros': 'cant_pasajeros',
     'asientos': 'cant_asientos',
     'vuelos': 'cant_vuelos'
}

df = df.rename(columns=columns_rename)

#merging columns
df['aeropuerto_origen']=df['aero_origen'] + ' - ' + df['origen_localidad'] 
df ['aeropuerto_destino']=df['aero_destino'] + ' - ' + df['destino_localidad']

#drop unnecesary columns after merging
df = df.drop(columns=['aero_origen', 'origen_localidad','aero_destino', 'destino_localidad'])

#drop null, empty or duplicate rows
df = df.dropna()
df = df.drop_duplicates()

#build an array with all columns (object type)
transform_columns = df.select_dtypes(include=['object']).columns.tolist()
df [transform_columns] = df[transform_columns].astype('string')

print(df.info())