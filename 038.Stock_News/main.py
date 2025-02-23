import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "Your API Key"
NEWS_API_KEY = "Your API Key"
TWILIO_SID = "Your SID"
TWILIO_AUTH_TOKEN = "Your Auth Token"

# Getting Yesterday's Stock closing price :
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Getting Day Before Yesterday's Stock closing price :
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Finding positive difference between 1 and 2 :
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0 :
    up_down = "🔺"
else:
    up_down = "🔻"

# Percentage difference in prices :
diff_percentage = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percentage)

# Check if diff_percentage is greater than 5, we have to get the news then :
if abs(diff_percentage) > 1:
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_article = news_response.json()["articles"]
    
    three_articles = news_article[:3]

    # Creating a list of first three articles's headline and description :
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    # Send news through Twilio
    client  = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="Your Number",
            to="Target Number"
        )