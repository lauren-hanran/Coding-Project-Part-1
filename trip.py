# need classes
# try and except

class Error(Exception):
    def __init__(self, value ):
        super(). __init__

    def amount(self, amount):
        if amount < 0:
            raise AmountError("can't have negative amount of money")
 #raise exceptions when my code generates run-time error

class Country:
    def __init__(self, name, country_code, currency_symbol):
     self.country_name = name
     self.country_code = country_code
     self.currency_symbol = currency_symbol
#create initialiser method to defore 3 values for new Country object
#create method that takes amount of money and returns money rounded to nearest cent
#create an overloaded version of the special __str__ fn,
#  that returns a strong counting the country details
    def format_country(self, ):



class Details:
    def __init__(self, places):
        self.places = []
        self.add_place = str(input(""))



