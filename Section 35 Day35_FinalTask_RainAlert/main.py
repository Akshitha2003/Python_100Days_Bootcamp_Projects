import requests
import smtplib

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "6d3dbbc9ab7b6e9729c01c2a4f6472da"
weather_params = {
    "lat": 54.012920,
    "lon": -128.629120,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="testuser1udemy@gmail.com", password="ccnwwannsltwuxsp")
        connection.sendmail(msg="Subject:Rain Alert!!!\n\nIt's going to rain today. Remember to bring an umbrella",
                            from_addr="testuser1udemy@gmail.com",
                            to_addrs="testuser1udemy@gmail.com")

