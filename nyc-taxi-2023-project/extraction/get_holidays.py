import requests,json,os

country_code = "US"
year = 2023

#holidays
public_holiday = f"https://nagerholidays.com/api/v3/PublicHolidays/{year}/{country_code}"
response_holiday = requests.get(public_holiday)

#save the json in raw layout
folder="nyc-taxi-2023-project/data/raw/holidays"
os.makedirs(folder, exist_ok=True) #check if the folder exists

filepath=os.path.join(folder, "holiday_data.json")

with open ( filepath , "w" ) as file: 
    json.dump(response_holiday.json(), file)

