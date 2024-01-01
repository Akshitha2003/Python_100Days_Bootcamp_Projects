import requests
from flight_search import FlightSearch

ENDPOINT = "https://api.sheety.co/b864df17c1c3de9cd0e9ec42ec556e7f/flightDeals/prices"
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
        response = requests.get(url=ENDPOINT, headers=self.headers)
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
                response = requests.put(url=f"{ENDPOINT}/{city['id']}", json=update_flight_deal_data,
                                        headers=self.headers)
                response.raise_for_status()
        self.get_flight_deal_data()
