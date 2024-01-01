# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
# import pandas


data_manager = DataManager()
data_manager.update_flight_iata()
flight_deal_data = data_manager.flight_deal_data["prices"]
# flight_deal_data = pandas.read_csv("Flight Deals - prices.csv").to_dict(orient="records")

suitable_flights = []
for city in flight_deal_data:
    flight_details = FlightSearch().get_flight_details(city["iataCode"])
    if int(flight_details[0]["price"]) <= int(city["lowestPrice"]):
        suitable_flights.append(FlightData(dep_code=flight_details[0]["flyFrom"],
                                           des_code=flight_details[0]["flyTo"],
                                           dep_city=flight_details[0]["cityFrom"],
                                           des_city=flight_details[0]["cityTo"],
                                           flight_price=flight_details[0]["price"],
                                           flight_from_date=flight_details[0]["route"][0]["local_departure"].split("T")[0],
                                           flight_to_date=flight_details[0]["route"][1]["local_departure"].split("T")[0]
                                           )
                                )
if len(suitable_flights) != 0:
    for details in suitable_flights:
        notification = NotificationManager(details)
