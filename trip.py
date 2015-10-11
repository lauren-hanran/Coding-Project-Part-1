__author__ = 'Lauren Hanran'


class Error(Exception):
    """ not really sure wtf this does """

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

    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        tuple_details = (country_name, start_date, end_date)
        start_list = start_date.split('/')
        end_list = (end_date.split('/'))                # if not start_list.isdigit() and not end_list.isdigit():
        for element in start_list:
            if element.isdigit() == False:
                raise Error("Start Date isn't formatted properly")
        for element in end_list:
            if element.isdigit() == False:
                raise Error("End Date isn't formatted properly")
        for item in start_date:
            if len(item[0]) == 4 and len(item[1]) == 2 and len(item[2] == 2):
                if start_date > end_date:
                    raise ValueError("Start date is greater than end date")
                if start_date in tuple_details:
                    raise Error("Can't travel more than one country per day")
        else:
            self.locations.append(tuple_details)
        return self.locations


    def current_country(self, date_string):
            for part in self.locations:
                if part[1] < date_string < part[2]:
                    return part[0]



    def is_empty(self):
        return self.locations == []

# country_details = Country(input("enter Country name: "), input("enter Country code: "), input("enter currency symbol: ")).round_money(100.10)
# print(country_details)  # create first object of country class
details = Details()
holiday_details = details.add("Australia", "2015/12/19", "2015/12/31")
print(holiday_details)
