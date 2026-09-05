import requests, json,os

country_code = "US"
year = 2023

#long holidays
long_holiday = f"https://nagerholidays.com/api/v3/LongWeekend/{year}/{country_code}"
response_long = requests.get(long_holiday)

#save the json in raw layout
folder="nyc-taxi-2023-project/data/raw/holidays"
os.makedirs(folder, exist_ok=True) #check if the folder exists

filepath=os.path.join(folder, "long_holiday_data.json")

with open ( filepath , "w" ) as file: 
    json.dump(response_long.json(), file)
    
    git commit -m "I downloaded a JSON file from nager holiday with 2023 long holidays"