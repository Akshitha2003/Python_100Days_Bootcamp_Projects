import requests
from flight_search import FlightSearch

SHEETY_PRICE_ENDPOINT = "https://api.sheety.co/b864df17c1c3de9cd0e9ec42ec556e7f/flightDeals/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/b864df17c1c3de9cd0e9ec42ec556e7f/flightDeals/users"
TOKEN = "Hellothisisanewyear2024"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {TOKEN}"
        }
        self.flight_deal_data = {}
        self.get_flight_deal_data()

    def get_flight_deal_data(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        self.flight_deal_data = response.json()

    def update_flight_iata(self):
        """
        Updates the missing IATA Codes of each city in the Excel.
        """
        for city in self.flight_deal_data["prices"]:
            if city["iataCode"] == "":
                update_flight_deal_data = {
                    "price": {
                        "iataCode": FlightSearch().get_destination_code(city["city"])
                    }
                }
                response = requests.put(url=f"{SHEETY_PRICE_ENDPOINT}/{city['id']}", json=update_flight_deal_data,
                                        headers=self.headers)
                response.raise_for_status()
        self.get_flight_deal_data()

    def post_user_details(self):
        """
        Post the user details to the Google Sheet.
        :return: Dictionary
        """
        print("Welcome to Akshitha's Flight Club.\nWe find the best flight deals and email you.")
        first_name = input("What is your first name?\n").title()
        last_name = input("What is your last name?\n").title()
        email = input("What is your email?\n")
        email_again = input("Type your email again.\n")
        if email == email_again:
          print("You're in the club!")
          new_data = {
            "user": {
              "firstName": first_name,
              "lastName": last_name,
              "email": email
            }
          }
          response = requests.post(url=SHEETY_USER_ENDPOINT, json=new_data, headers = self.headers)
          response.raise_for_status()

    def get_user_details(self):
        """
        Retrieves the user details from the Google Sheet.
        :return: Dictionary
        """
        response = requests.get(url=SHEETY_USER_ENDPOINT, headers = self.headers)
        response.raise_for_status()
        return response.json()["users"]
      