import os
import pandas as pd

from transformation.transformation_holiday import normalize_name, cast_column
from load.load_bronze import df_to_parquet

#ENTITY HOLIDAY 
folder="nyc-taxi-2023-project/data/raw/holidays"
os.makedirs(folder, exist_ok=True) #check if the folder exists

filepath_1=os.path.join(folder, "holiday_data.json")
filepath_2=os.path.join(folder, "long_holiday_data.json")

df=pd.read_json(filepath_1)
df_holiday=normalize_name(df)
df_holiday=cast_column(df_holiday, 'local_name','object')
df_holiday=cast_column(df_holiday, 'name','object')


#ENTITY LONG HOLIDAY
df_long=pd.read_json(filepath_2)
df_long=normalize_name(df_long)

#ENTITY WEATHER
folder="nyc-taxi-2023-project/data/raw/"
os.makedirs(folder, exist_ok=True) #check if the folder exists

filepath_w=os.path.join(folder, "weather/Weather Information.csv")
df_2=pd.read_csv(filepath_w)
df_weather=normalize_name(df_2)
df_weather=cast_column(df_weather, 'date','date')
df_weather=cast_column(df_weather, 'station','string')
df_weather=cast_column(df_weather, 'name','string')

#TRANSFORM THE 3 DATAFRAME TO PARQUET FILE (ONE FOR EACH ENTITY)
output_dir="nyc-taxi-2023-project/data/bronze/"
output_holidays=os.path.join(output_dir, "holidays")
#df_to_parquet(df_holiday, output_holidays , 'holiday.parquet')
df_to_parquet(df_long, output_holidays , 'long_holidays.parquet')
