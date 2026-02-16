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
df['host_since']= pd.to_datetime(df['host_since'],format='%Y-%m-%d')
print(df.dtypes)
      
#https://www.youtube.com/playlist?list=PLxJ3eugu174JqpqulHkIf0wEmA2b5N5DF