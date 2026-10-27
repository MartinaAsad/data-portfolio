import os
import pandas as pd
import pyarrow.parquet as pq

from transformation.transformation_holiday import normalize_name, cast_column
from load.load_bronze import df_to_parquet
from transformation.transformation_taxis import normalize_name, cast_column, rename_column, add_date_column

#ENTITY HOLIDAY 
# folder="nyc-taxi-2023-project/data/raw/holidays"
# os.makedirs(folder, exist_ok=True) #check if the folder exists

# filepath_1=os.path.join(folder, "holiday_data.json")
# filepath_2=os.path.join(folder, "long_holiday_data.json")

# df=pd.read_json(filepath_1)
# df_holiday=normalize_name(df)
# df_holiday=cast_column(df_holiday, 'local_name','object')
# df_holiday=cast_column(df_holiday, 'name','object')


# # #ENTITY LONG HOLIDAY
# df_long=pd.read_json(filepath_2)
# df_long=normalize_name(df_long)

# # #ENTITY WEATHER
# folder="nyc-taxi-2023-project/data/raw/"
# os.makedirs(folder, exist_ok=True) #check if the folder exists

# filepath_w=os.path.join(folder, "weather/Weather Information.csv")
# df_2=pd.read_csv(filepath_w)
# df_weather=normalize_name(df_2)
# df_weather=cast_column(df_weather, 'date','date')
# df_weather=cast_column(df_weather, 'station','string')
# df_weather=cast_column(df_weather, 'name','string')

# # #TRANSFORM THE 3 DATAFRAME TO PARQUET FILE (ONE FOR EACH ENTITY)
# output_dir="nyc-taxi-2023-project/data/bronze/"
# output_holidays=os.path.join(output_dir, "holidays")
# df_to_parquet(df_holiday, output_holidays , 'holiday.parquet')
# df_to_parquet(df_long, output_holidays , 'long_holidays.parquet')

# output_weather=os.path.join(output_dir, "weather")
# df_to_parquet(df_weather, output_weather , 'weather.parquet')

#ENTITY TAXI (1 FILE BY MONTH)
folder="data/raw/taxis/"
output_dir = "data/bronze/taxis/"

for month in range(1,13):
    
    #read each Parquet by month
    filename = f"yellow_tripdata_2023-{month:02d}.parquet"
    filepath_1=os.path.join(folder, filename)
    df = pd.read_parquet(filepath_1)
    
    #for each file, make transformations
    norm=normalize_name(df)
    
    column_dict={"tpep_pickup_datetime":"pickup_datetime", "tpep_dropoff_datetime":"dropoff_datetime",
             "passenger_count":"passenger_amount", "ratecode_id":"final_rate_code", "pulocation_id":"tlc_engaged",
             "dolocation_id":"tlc_disengaged","tip_amount":"credit_card_tip"}
    
    norm =rename_column(norm, column_dict)
    norm = add_date_column(norm)

    column_cast={"passenger_amount":"Int64", "final_rate_code":"Int64","vendor_id": "int64",
    "tlc_engaged": "int64",
    "tlc_disengaged": "int64"}
    norm=cast_column(norm, column_cast)
    
    output_path = os.path.join(output_dir, filename)

    #save new parquet to bronze folder
    norm.to_parquet(
        output_path,
        engine="pyarrow",
        compression="snappy",
        index=False
    )


