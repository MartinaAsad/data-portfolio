import pandas as pd
import os,re

folder="nyc-taxi-2023-project/data/raw/"
os.makedirs(folder, exist_ok=True) #check if the folder exists

filepath_1=os.path.join(folder, "weather/Weather Information.csv")
df=pd.read_csv(filepath_1)
def normalize_name(df):
      df.columns= df.columns.str.lower() #transform column name to lower case
      return df

def cast_column(df,column_name, type):
    
    if(type=='date'):
       df[column_name] = pd.to_datetime(df[column_name])
    else:
        df[column_name] = df[column_name].astype('string')
    
df_2=normalize_name(df)
cast_column(df_2, 'date','date')
cast_column(df_2, 'station','string')
cast_column(df_2, 'name','string')

print(df_2[['station', 'date', 'name']].dtypes) #print the data type only in the modified columns