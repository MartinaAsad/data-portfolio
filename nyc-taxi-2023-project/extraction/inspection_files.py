import pandas as pd
import os, json


folder="nyc-taxi-2023-project/data/raw/"
os.makedirs(folder, exist_ok=True) #check if the folder exists

filepath_1=os.path.join(folder, "weather/Weather Information.csv")
filepath_2=os.path.join(folder, "holidays/holiday_data.json")
filepath_3=os.path.join(folder, "holidays/long_holiday_data.json")


def get_info(file_type, file):
    
    if(file_type=='csv'):
        df=pd.read_csv(file)
    else:
        with open (file, 'r', encoding='utf-8') as j:
            data = json.load(j)    
        df = pd.json_normalize(data)

    for column in df.columns: 
        print(f"Column: {column}, Type: {df[column].dtype}")
    
    #duplicated_rows = df.duplicated().sum()
    null_values = df.isna().sum()

    # 3. Show Results
    #print(f"Duplicated rowss: {duplicated_rows}\n")
    print("Null values by column:")
    print(null_values)
    
#to get information about weather file
get_info('csv',filepath_1)

#to get information about holiday file
#get_info('json',filepath_2)

#to get information about long holiday file
#get_info('json',filepath_3)