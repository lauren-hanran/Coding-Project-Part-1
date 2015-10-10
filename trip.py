# need classes
# try and except

class Error(Exception):

    def __init__(self, value):
        super(). __init__(value)
        self.value = value

    def amount(self, amount):
        if amount < 0 or amount != int:
            print ("Sorry not a valid amount")


class Country:
    """ Takes amount of money and returns money rounded to nearest cent"""
    def __init__(self, name, country_code, currency_symbol):
        self.country_name = name
        self.country_code = country_code
        self.currency_symbol = currency_symbol

    def round_money(self, money):
        print(self.amount)
        return self.currency_symbol + str(format(float(money), '.1f'))

    def __str__(self):
        return "Country. details" + str(self.country_name, self.country_code, self.currency_symbol


change something



class Details:

    def __init__(self, locations):
        self.locations = []
        self.country_name = locations
        self.start_date = []
        self.end_date = []
        self.date_string = []

    def add_details(self, country_name, start_date, end_date):
        self.country_name = []
        self.locations.append(country_name)

    def current_country(self, date_string):
        self.date_string = "YYYY/MM/DD"  # do something to make string in date format

    def is_empty(self, ):
        return ()

