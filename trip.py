# need classes
# try and except

class Error(Exception):
    def __init__(self, value):
        super(). __init__

    def amount(self, amount):
        if amount < 0:
            raise AmountError("Can't have negative amount of money")
 #raise exceptions when my code generates run-time error

class Country:
    def __init__(self, name, country_code, currency_symbol):
     self.country_name = name
     self.country_code = country_code
     self.currency_symbol = currency_symbol
#create initialiser method to define 3 values for new Country object
#create method that takes amount of money and returns money rounded to nearest cent
#create an overloaded version of the special __str__ fn,
#  that returns a strong counting the country details
    def format_country(self, ):



class Details:

    def __init__(self, locations):
        self.places = locations
        self.places = []
        country_name = str(country_name)

    def add_place(self, place):
        self.places.append(place)

    def add_details(self, country_name, start_date, end_date):
        self.country_name = []
        self.country_name.append(country_name)

    def current_country(self, date_string):
        #do something to make string in date format

    def is_empty(self, ):






