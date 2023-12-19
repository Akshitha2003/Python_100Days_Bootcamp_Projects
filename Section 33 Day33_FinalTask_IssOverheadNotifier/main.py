import requests
from datetime import datetime
import smtplib

MY_LAT = 13.082680
MY_LONG = 80.270721

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
# MY_LAT = iss_latitude+3
# MY_LONG = iss_longitude+2

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
time_hour = time_now.hour
print(sunset)
print(sunrise)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds. (--> Refer Original python script)
if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    if sunset >= time_hour <= sunrise:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="testuser1udemy@gmail.com", password="ccnwwannsltwuxsp")
            connection.sendmail(from_addr="testuser1udemy@gmail.com",
                                to_addrs="testuser2udemy@yahoo.com",
                                msg="Subject:ISS is overhead\n\nLook up.")
