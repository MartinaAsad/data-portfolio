
def drop_columns(df, list_columns):
    df=df.drop(columns=[list_columns])
    return df

def drop_rows(df, column):
    #analyse only rows in year 2013
    new_df= df.loc[(df[column] >= '2023-09-01')
                     & (df[column] < '2024-01-01')]
    return new_df