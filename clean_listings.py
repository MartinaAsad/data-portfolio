import pandas as pd
    
df=pd.read_csv('dataset/Airbnb Data/Listings.csv', encoding="mac_roman")

#count: 279712
#drop null values
df.dropna(subset=['listing_id'])

# #drop duplicate values
df.drop_duplicates()

# #drop unnecesary columns
columns =['host_response_rate','host_acceptance_rate','host_is_superhost','host_has_profile_pic', 'host_identity_verified',
          'latitude', 'longitude', 'accommodates','review_scores_accuracy', 'review_scores_communication',
          'review_scores_value', 'instant_bookable']

df= df.drop(columns, axis=1)

#change the data type of columns
df['host_since']= pd.to_datetime(df['host_since'],format='%d/%m/%Y')

object_cols=df.select_dtypes(include=['object']).columns
df[object_cols]=df[object_cols].astype('string')

#rename columns
df_updated= df.rename(columns={'name':'name_listings',
                               'host_location':'host_address',
                               'host_response_time':'host_response_hours'})

#replace information
replace_dict={'a few days or more': '72',
              'within a day':'24',
              'within a few hours':'12',
              'within an hour':'1'
              }

df_updated['host_response_hours']=df_updated['host_response_hours'].replace(replace_dict)

df_updated['host_response_hours']=df_updated['host_response_hours'].fillna('No Activity')

df_updated.to_parquet('dataset/Airbnb Data/listings.parquet', engine='fastparquet', compression='snappy', index=False)

#https://www.youtube.com/playlist?list=PLxJ3eugu174JqpqulHkIf0wEmA2b5N5DF