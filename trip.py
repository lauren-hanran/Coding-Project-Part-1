__author__ = 'Lauren Hanran'


class Error(Exception):
    def __init__(self, value):
        super(). __init__(value)


class Country:
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
        # separate dates by '/' and check that dates are in the right date format before adding them to the list
        start_list = start_date.split('/')
        end_list = (end_date.split('/'))
        for element in start_list:
            if not element.isdigit():  # check that each part in the date is a number
                raise Error("Start Date isn't formatted properly")
        for element in end_list:
            if not element.isdigit():
                raise Error("End Date isn't formatted properly")
        if start_date > end_date:
            raise Error("Start date is greater than end date")
        for item in start_date:
            if len(item[0]) == 4 and len(item[1]) == 2 and len(item[2]) == 2:
                if start_date in tuple_details:
                    raise Error("Can't travel more than one country per day")
        else:
            self.locations.append(tuple_details)
        return self.locations

    def current_country(self, date_string):
        for part in self.locations:
            if part[1] <= date_string <= part[2]:
                return part[0]
        raise Error("Date is not found")

    def is_empty(self):
        return self.locations == []


def main():
    details = Details()
    print("Error with Start_date")
    try:
        details.add("Australia", "201/12/19", "2015/12/31")  # when year is too short
    except Error as error:
        print(error)
    try:
        details.add("Australia", "20156/12/19", "2015/12/31")  # when year is too long
    except Error as error:
        print(error)

    print("\nError with End_date")
    try:
        details.add("Australia", "201/12/19", "2015/12/31")  # year
    except Error as error:
        print(error)
    try:
        details.add("Australia", "20156/12/19", "2015/12/31")
    except Error as error:
        print(error)

    print("\nError with date values")
    try:
        details.add("Australia", "2015/12/19", "2015/12/19")  # year
    except Error as error:
        print(error)

if __name__ == "__main__":
    main()
