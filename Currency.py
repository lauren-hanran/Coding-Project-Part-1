import web_utility


def convert(amount, home_currency_code, location_currency_code):
    url = "https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + home_currency_code + "&to=" + location_currency_code
    try:
        result = web_utility.load_page(url)
        split_string = result[result.index('result'):]
        # print(result[result.index('result'):])
        split_string = split_string.split(">")  # split the function into parts by using '>'
        split_string = split_string[2].split(" ")  # split the parts again into smaller sections
        return float(split_string[0])

    except:             # if there is any error, eg. page doesn't load, it will return -1
        return -1


def get_details(country_name):  # get the country name as a string and return the value as a tuple in parts

    country_name = str(country_name.title())
    input_file = open('currency_details.txt', mode='r', encoding='UTF-8')  # open file for reading

    for line in input_file:
        parts = line.strip().split(',')

        if parts[0] == country_name:
            input_file.close()
            return tuple(parts)

    input_file.close()
    return ()

details = get_details(input("Enter Country Name: "))
print(details)

value = convert(input("Enter amount: "), input("Enter home currency code: "), input("Enter location currency code: "))
print(value)
