import pandas as pd

df= pd.read_parquet('dataset/Airbnb Data/listings.parquet')

''''listing_id', 'name_listings', 'host_id', 
'host_since', 'host_address',
       'host_response_hours', 'host_total_listings_count',
       'neighbourhood', 'district', 'city', 'property_type',
       'room_type', 'bedrooms',
       'amenities', 'price', 'minimum_nights',
       'maximum_nights',
       'review_scores_rating', 'review_scores_cleanliness',
       'review_scores_checkin', 'review_scores_location']'''
masc1=df.groupby('city')
masc2=df.groupby('property_type')

mean_price=masc1['price'].mean()
mean_rating=masc2['review_scores_rating'].mean()

#barrios por ciudad
city_neigh=masc1['neighbourhood'].unique()


print('El rating promedio de los alquileres es: ', mean_rating)
#print('Los puntajes pueden ser entre: ',df['review_scores_rating'].unique())
print('Los barrios que hay por cada ciudad son: ',city_neigh)
#print(df[df['review_scores_rating'].isna()])