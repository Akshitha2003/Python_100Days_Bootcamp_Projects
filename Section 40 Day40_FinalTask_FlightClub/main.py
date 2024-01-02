# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

# Deployed Link - https://replit.com/@akshithamaryac2/FlightClubProject2?v=1
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
# import pandas


data_manager = DataManager()
data_manager.update_flight_iata()
flight_deal_data = data_manager.flight_deal_data["prices"]
# flight_deal_data = pandas.read_csv("Flight Deals - prices.csv").to_dict(orient="records")
data_manager.post_user_details()

suitable_flights = []
for city in flight_deal_data:
    flight_details = FlightSearch().get_flight_details(city["iataCode"])
    if flight_details is not None and int(flight_details["price"]) <= int(city["lowestPrice"]) and len(flight_details["route"])==2:
        suitable_flights.append(FlightData(dep_code=flight_details["flyFrom"],
                                           des_code=flight_details["flyTo"],
                                           dep_city=flight_details["cityFrom"],
                                           des_city=flight_details["cityTo"],
                                           flight_price=flight_details["price"],
                                           flight_from_date=flight_details["route"][0]["local_departure"].split("T")[0],
                                           flight_to_date=flight_details["route"][1]["local_departure"].split("T")[0]
                                           )
                                )
    if flight_details is not None and int(flight_details["price"]) <= int(city["lowestPrice"]) and len(flight_details["route"])==4:
        suitable_flights.append(FlightData(dep_code=flight_details["flyFrom"],
                   des_code=flight_details["flyTo"],
                   dep_city=flight_details["cityFrom"],
                   des_city=flight_details["cityTo"],
                   flight_price=flight_details["price"],
                   flight_from_date=flight_details["route"][0]["local_departure"].split("T")[0],
                   flight_to_date=flight_details["route"][2]["local_departure"].split("T")[0],
                   stop_over=1,
                   via_city=flight_details["route"][1]["cityFrom"]
                   )
                   
        )
if len(suitable_flights) != 0:
    for details in suitable_flights:
        notification = NotificationManager(details)
        user_details = data_manager.get_user_details()
        for user in user_details:
            notification.send_mail(details, user["email"])
        