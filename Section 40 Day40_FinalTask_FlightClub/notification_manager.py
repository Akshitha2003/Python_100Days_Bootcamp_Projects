import smtplib
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env

MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")
TWILIO_PHONE_NO = os.getenv("TWILIO_PHONE_NUMBER")
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, details):
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user="testuser1udemy@gmail.com", password="ccnwwannsltwuxsp")
        #     message = (f"Low price alert! Only £{details.flight_price} to fly from {details.departure_city}-"
        #                f"{details.departure_code} to {details.destination_city}-{details.destination_code}, from "
        #                f"{details.flight_from_date} to {details.flight_to_date}.")
        #     connection.sendmail(from_addr="testuser1udemy@gmail.com",
        #                         to_addrs="testuser1udemy@gmail.com",
        #                         msg=message.encode(encoding='utf-8', errors='strict'))
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        text = (f"Low price alert! Only £{details.flight_price} to fly from {details.departure_city}-"
                f"{details.departure_code} to {details.destination_city}-{details.destination_code}, from"
                f" {details.flight_from_date} to {details.flight_to_date}.")
        if details.stop_over == 1:
            text += f"\nFlight has 1 stop over, via {details.via_city} city."
        message = client.messages.create(
            from_=TWILIO_PHONE_NO,
            body=text,
            to=MY_PHONE_NUMBER
        )
        print(message.status)

    def send_mail(self, details, to_user):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="testuser1udemy@gmail.com", password="ccnwwannsltwuxsp")
            message = (f"Low price alert! Only £{details.flight_price} to fly from {details.departure_city}-"
                       f"{details.departure_code} to {details.destination_city}-{details.destination_code}, from "
                       f"{details.flight_from_date} to {details.flight_to_date}.")
            if details.stop_over == 1:
                message += f"\nFlight has 1 stop over, via {details.via_city} city."
            connection.sendmail(from_addr="testuser1udemy@gmail.com",
                                to_addrs=to_user,
                                msg=message.encode(encoding='utf-8', errors='strict'))
          