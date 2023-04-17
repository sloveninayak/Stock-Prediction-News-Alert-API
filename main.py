import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "342ILY4WK3O67SR3"
NEW_API_KEY = "ea3c4cb833b54e5dbc09cc0e95ba7e9f"
TWILIO_SID = "Ahfwuicfhkuergfkhegfhkergfhjgfr"
TWILIO_AUTH_TOKEN = "lkfnjkafkjfjefhukerfhuakfa"

stock_params = {
    "function=TIME_SERIES_INTRADAY"
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()[""]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)
difference = float(yesterday_closing_price - day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)
if diff_percent > 1:
    news_params = {
        "apiKey" : NEW_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
   articles = news_response.json()["articles"]
   print(articles)
three_articles = articles[:3]
print(three_articles)

formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article[description]}" for article in three_articles]
client = Client(TWILIO_sid, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.message.create(
        body = article,
        from = "+911234567890",
        to = "+91572895725"
)
