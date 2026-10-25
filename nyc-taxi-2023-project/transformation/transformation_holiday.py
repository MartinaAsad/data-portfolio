import pandas as pd
import os,re

def normalize_name(df):
    
    #transform camelCase to snake_case
       df.columns = (
        df.columns
        .str.replace(r'([a-z])([A-Z])', r'\1_\2', regex=True)
        .str.lower()
    )
       return df

def cast_column(df,column_name, type):
    
    #object transform to array type
    if('name' in column_name and type=='object'):
       df[column_name] = df[column_name].astype('string')
    elif ('date' in column_name and type=='object'):
       df[column_name] = pd.to_datetime(df[column_name])
       
    return df


#testing both emthods
    
# df_2=normalize_name(df)
# df_3=normalize_name(df_long)
# #print(df.dtypes)
# print(df_long.dtypes)

# cast_column(df_2, 'local_name','object')
# cast_column(df_2, 'name','object')

#print(df_2[['local_name', 'name']].dtypes) #print the data type only in the modified columns
#print('algo',df_2[['date']].dtypes) #print the data type only in the modified columns