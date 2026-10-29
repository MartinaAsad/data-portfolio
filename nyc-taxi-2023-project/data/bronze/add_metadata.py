import os
import pyarrow.parquet as pq
import pandas as pd
from methods_add_metadata import add_ingestion_date, add_batch_id, add_source, delete_folder
#ENTITY HOLIDAY

# folder_1="data/bronze/holidays"
# os.makedirs(folder_1, exist_ok=True)

# filepath_1=os.path.join(folder_1, "holiday.parquet")
# filepath_2=os.path.join(folder_1, "long_holidays.parquet")

# # Read holiday parquet file
# df_holiday = pd.read_parquet(filepath_1)

# #add metadata on holiday file
# df_holiday=add_ingestion_date(df_holiday)
# df_holiday=add_batch_id(df_holiday)
# df_holiday= add_source(df_holiday,"holiday_data.json")

# # Read long holiday parquet file
# df_long_holiday = pd.read_parquet(filepath_2)

# #add metadata on long holiday file
# df_long_holiday=add_ingestion_date(df_long_holiday)
# df_long_holiday=add_batch_id(df_long_holiday)
# df_long_holiday= add_source(df_long_holiday,"long_holiday_data.json")


#ENTITY TAXI (1 FILE BY MONTH)
folder_2="data/bronze/taxis/"
output_dir = "data/bronze/taxis/"

for month in range(1,13):
    
    #read each Parquet by month
    filename = f"yellow_tripdata_2023-{month:02d}.parquet"
    filepath_1=os.path.join(folder_2, filename)
    print(f"Procesando: {filename}")
    
    df = pd.read_parquet(filepath_1)
    
    #for each file, make transformations
    df= add_batch_id(df)
    df= add_source(df,filename)
    output_path = os.path.join(output_dir, filename)

    #save new parquet to bronze folder
    df.to_parquet(
        output_path,
        engine="pyarrow",
        compression="snappy",
        index=False
    )
    print('entro')

# df_holiday.to_parquet(filepath_1, engine='pyarrow', compression='snappy', index=False)
# df_long_holiday.to_parquet(filepath_2, engine='pyarrow', compression='snappy', index=False)