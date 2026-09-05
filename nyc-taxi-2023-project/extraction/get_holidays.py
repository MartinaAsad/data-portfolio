import requests

country_code = "US"
year = 2023

#holidays
public_holiday = f"https://nagerholidays.com/api/v3/PublicHolidays/{year}/{country_code}"
response_holiday = requests.get(public_holiday)

if response_holiday.status_code == 200:
    holidays = response_holiday.json()
    for h in holidays:
        print(h["date"], "-", h["name"])
else:
    print("Error:", response_holiday.status_code, response_holiday.text)

