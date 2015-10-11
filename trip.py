__author__ = 'Lauren Hanran'


class Error(Exception):

    def __init__(self, value):
        super(). __init__(value)


class Country:
    """ Takes amount of money and returns it rounded to nearest cent"""
    def __init__(self, name, country_code, currency_symbol):
        self.country_name = name
        self.country_code = country_code
        self.currency_symbol = currency_symbol

    def round_money(self, money):
        return self.currency_symbol + str(format(float(money), '.2f'))

    def __str__(self):
        return "Country details: " + "{} {} {}".format(str(self.country_name), str(self.country_code), str(self.currency_symbol))


class Details:

    def __init__(self, locations):
        self.locations = []

    def add_details(self, country_name, start_date, end_date):
        self.locations.append(country_name)  # add country name to list
        tuple_details = (country_name, start_date, end_date)
        self.locations.append(tuple_details)

    def current_country(self, date_string):
        for part in self.locations:
            if part[1] < date_string < part[2]:
                return part[0]

    def is_empty(self):
        return self.locations == []

country_details = Country(input("enter Country name: "), input("enter Country code: "), input("enter currency symbol: ")).round_money(100.10)
print(country_details)

holiday_details = ("Australia", "19/12/2015", "31/12/2015")
# create first object of country class
