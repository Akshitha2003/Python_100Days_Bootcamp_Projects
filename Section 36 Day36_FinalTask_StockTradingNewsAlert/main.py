import requests
import smtplib


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "BXBO2HB9QOSTCHKP"
NEWS_API_KEY = "8a6cf5d03df64fbf8411aca437c6c776"

# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_api_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

stock_price = []
for data in stock_data.values():
    if len(stock_price) == 2:
        break
    stock_price.append(float(data["4. close"]))

stock_price_percent = (stock_price[1]-stock_price[0])/stock_price[0]*100
if -5 <= stock_price_percent <= 5:

    # # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_api_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_api_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    news_data_title = [news["title"] for news in news_data]
    news_data_description = [news["description"] for news in news_data]

    # # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="testuser1udemy@gmail.com", password="ccnwwannsltwuxsp")
        connection.sendmail(from_addr="testuser1udemy@gmail.com",
                            to_addrs="testuser1udemy@gmail.com",
                            msg=f"Subject:{STOCK}: {round(stock_price_percent)}%\n\n"
                                f"Headline: {news_data_title[0]}\nBrief: {news_data_description[0]}"
                            )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

