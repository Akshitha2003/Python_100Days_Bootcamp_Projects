class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, dep_code, des_code, dep_city, des_city, flight_price, flight_from_date, flight_to_date):
        self.departure_code = dep_code
        self.destination_code = des_code
        self.departure_city = dep_city
        self.destination_city = des_city
        self.flight_price = flight_price
        self.flight_from_date = flight_from_date
        self.flight_to_date = flight_to_date
