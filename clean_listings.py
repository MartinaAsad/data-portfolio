import pandas as pd

arch1=pd.read_csv('dataset/Airbnb Data/Listings.csv', encoding='unicode_escape')
'''Data columns (total 33 columns):
 #   Column                       Non-Null Count   Dtype
---  ------                       --------------   -----
 0   listing_id                   279712 non-null  int64
 1   name                         279537 non-null  object
 2   host_id                      279712 non-null  int64
 3   host_since                   279547 non-null  object
 4   host_location                278872 non-null  object
 5   host_response_time           150930 non-null  object
 6   host_response_rate           150930 non-null  float64
 7   host_acceptance_rate         166625 non-null  float64
 8   host_is_superhost            279547 non-null  object
 9   host_total_listings_count    279547 non-null  float64
 10  host_has_profile_pic         279547 non-null  object
 11  host_identity_verified       279547 non-null  object
 12  neighbourhood                279712 non-null  object
 13  district                     37012 non-null   object
 14  city                         279712 non-null  object
 15  latitude                     279712 non-null  float64
 16  longitude                    279712 non-null  float64
 17  property_type                279712 non-null  object
 18  room_type                    279712 non-null  object
 19  accommodates                 279712 non-null  int64
 20  bedrooms                     250277 non-null  float64
 21  amenities                    279712 non-null  object
 22  price                        279712 non-null  int64
 23  minimum_nights               279712 non-null  int64
 24  maximum_nights               279712 non-null  int64
 25  review_scores_rating         188307 non-null  float64
 26  review_scores_accuracy       187999 non-null  float64
 27  review_scores_cleanliness    188047 non-null  float64
 28  review_scores_checkin        187941 non-null  float64
 29  review_scores_communication  188025 non-null  float64
 30  review_scores_location       187937 non-null  float64
 31  review_scores_value          187927 non-null  float64
 32  instant_bookable             279712 non-null  object'''

      



#https://www.youtube.com/playlist?list=PLxJ3eugu174JqpqulHkIf0wEmA2b5N5DF