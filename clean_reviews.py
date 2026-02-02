import pandas as pd

arch2=pd.read_csv('dataset/Airbnb Data/Reviews.csv', encoding='unicode_escape')
'''RangeIndex: 5373143 entries, 0 to 5373142
Data columns (total 4 columns):
 #   Column       Dtype 
---  ------       ----- 
 0   listing_id   int64 
 1   review_id    int64 
 2   date         object
 3   reviewer_id  int64 '''