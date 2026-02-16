import pandas as pd
import chardet

with open('dataset/Airbnb Data/Listings.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding_type = result['encoding']
    print(f"Detected encoding: {encoding_type}")
    
df=pd.read_csv('dataset/Airbnb Data/Listings.csv', encoding=encoding_type)

#count: 279712
#drop null values
df.dropna(subset=['listing_id'])

#drop duplicate values
df.drop_duplicates()

#drop unnecesary columns
columns =['host_id','host_response_rate','host_acceptance_rate','host_has_profile_pic', 'host_identity_verified',
          'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication',
          'review_scores_location', 'review_scores_value', 'instant_bookable']

print(df['name'])
      
#https://www.youtube.com/playlist?list=PLxJ3eugu174JqpqulHkIf0wEmA2b5N5DF