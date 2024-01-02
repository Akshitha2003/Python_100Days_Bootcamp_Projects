import requests
from datetime import datetime, timedelta

ENDPOINT = "https://api.tequila.kiwi.com"
API_KEY = "3oS8DvnECF9PIS9Pr4XHlIS2SPO1s7Px"
today = datetime.now() + timedelta(days=1)
from_date = today.strftime("%d/%m/%Y")
six_months_later = datetime.now() + timedelta(days=6*30)
to_date = six_months_later.strftime("%d/%m/%Y")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            "apikey": API_KEY
        }

    def get_destination_code(self, city_name):
        """
        Retrieves the IATA code
        :param city_name:
        :return: String
        """
        tequila_location_endpoint = f"{ENDPOINT}/locations/query"
        parameters = {
            "term": city_name,
            "location_type": "city"
        }
        response = requests.get(url=tequila_location_endpoint, headers=self.headers, params=parameters)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def get_flight_details(self, city_code):
        tequila_search_endpoint = f"{ENDPOINT}/v2/search"
        parameters = {
            "fly_from": "LON",
            "fly_to": city_code,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0
        }
        response = requests.get(url=tequila_search_endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()
        try:
            return_data = response.json()["data"][0]
        except IndexError:
            # print(f"No direct flight found for {city_code}.")
            parameters["max_stopovers"] = 2
            response = requests.get(url=tequila_search_endpoint, params=parameters, headers=self.headers)
            response.raise_for_status()
            try:
                return_data = response.json()["data"][0]
            except IndexError:
                # print(f"No stopover routes found for {city_code}")
                return None
            else:
                return return_data
        else:
            return return_data
