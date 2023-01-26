import requests


print("**************WELCOME TO STOCK PRISE APP********************")
COMPANY_NAME = input("Which company are you looking for ?\n Tesla / Apple / Microsoft => ").title()
STOCK_NAME = ""


if COMPANY_NAME == "Tesla":
    STOCK_NAME += "TSLA"
elif COMPANY_NAME == "Apple":
    STOCK_NAME += "APPL"
elif COMPANY_NAME == "Microsoft":
    STOCK_NAME += "MSFT"
else:
    print("This company is not in list")
    exit(0)

    
    
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

STOCK_API_KEY = "4V3L*********" #USE YOUR OWN API KEY


stock_params = {
    "function": "TIME_SERIES_WEEKLY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Weekly Time Series']
data_list = [value for (key, value) in data.items()]


This_week_data = data_list[0]
This_week_closing_prize = This_week_data['4. close']


day_before_This_week_data = data_list[1]
day_before_This_week_closing_prize = day_before_This_week_data['4. close']


difference = float(This_week_closing_prize) - float(day_before_This_week_closing_prize)
difference_percentage = abs((difference / float(day_before_This_week_closing_prize)) * 100)

print(f" This week Stock closing prise = {This_week_closing_prize}$")
print(f"Previous week Stock closing prise = {day_before_This_week_closing_prize}$")
print(f"Total fluctuation = {round(difference, 3)}$")
print(f"Total fluctuation Percentage = {round(difference_percentage, 3)}$")
