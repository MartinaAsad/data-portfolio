import pandas as pd


df = pd.read_csv('aeropuertos_arg_limpio.csv')

#nombres de columna sy tipos de datos
print("tipos",df.dtypes)
print("columnas",df.columns)