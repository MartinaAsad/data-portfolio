import os
import pyarrow.parquet as pq
from datetime import datetime

def normalize_name(df):
     df.columns = (
             df.columns
             .str.replace(r'([a-z])([A-Z])', r'\1_\2', regex=True)
             .str.lower()
         ) #transform column name to lower case and snake_case
     return df
  
def rename_column(df, column_dict):
    for k,v in column_dict.items():
        df=df.rename(columns={
        k: v
        })
    
    return df

def add_date_column(df):
    df["entry_date"] = datetime.now()
    return df

def cast_column(df, column_dict):
    for k,v in column_dict.items():
        df[k] = df[k].astype(v)
            
    return df

