__author__ = 'Lauren Hanran'


class Error(Exception):
    def __init__(self, value):
        super(). __init__(value)


class Country: # holds the country details and displays
    def __init__(self, name, country_code, currency_symbol):
        self.country_name = name
        self.country_code = country_code
        self.currency_symbol = currency_symbol

    def round_money(self, money):
        return self.currency_symbol + str(format(float(money), '.2f'))

    def __str__(self):  # overloaded
        return "Country details: " + "{} {} {}".format(str(self.country_name), str(self.country_code), str(self.currency_symbol))


class Details:

    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        tuple_details = (country_name, start_date, end_date)
        # separate dates by '/' and check that dates are in the right date format before adding them to the list
        start_list = start_date.split('/')
        end_list = end_date.split('/')
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

    print("Test for Country Class")   #ensure that Country class works
    try:
        saudi_arabia = Country('Saudi Arabia', 'SAR', '﷼')
        print(saudi_arabia.round_money(109.987))
    except Error as error:
        return "Error with Country Class"

    details = Details()
    print("\nTest for Details Class")
    print("Error with Start_date")
    try:  # when year is too short
        details.add("Australia", "201/12/19", "2015/12/31")
    except Error as error:
        print(error)
    try:   # when year is too long
        details.add("Australia", "20156/12/19", "2015/12/31")
    except Error as error:
        print(error)
    try:  # when month is too short
        details.add("Australia", "2015/1/19", "2015/12/31")
    except Error as error:
        print(error)
    try:  # when month is too long
        details.add("Australia", "2015/111/19", "2015/12/31")
    except Error as error:
        print(error)
    try:  # when day is too short
        details.add("Australia", "2015/12/1", "2015/12/31")
    except Error as error:
        print(error)
    try:  # when day is too long
        details.add("Australia", "2015/12/199", "2015/12/31")
    except Error as error:
        print(error)

    print("\nError with End_date")
    try:  # when year is too short
        details.add("Australia", "2015/12/19", "201/12/31")
    except Error as error:
        print(error)
    try:  # when year is too long
        details.add("Australia", "2015/12/19", "20156/12/31")
    except Error as error:
        print(error)
    try:  # when month is too short
        details.add("Australia", "2015/12/19", "2015/1/31")
    except Error as error:
        print(error)
    try:  # when month is too long
        details.add("Australia", "2015/12/19", "2015/123/31")
    except Error as error:
        print(error)
    try:  # when day is too short
        details.add("Australia", "2015/12/19", "2015/1/311")
    except Error as error:
        print(error)
    try:  # when day is too long
        details.add("Australia", "2015/12/19", "2015/123/3")
    except Error as error:
        print(error)



if __name__ == "__main__":
    main()
