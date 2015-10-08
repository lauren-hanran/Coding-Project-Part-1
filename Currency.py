import web_utility


def convert(amount, home_currency_code, location_currency_code):
    url = str("https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + home_currency_code + "&to=" + location_currency_code)
    result = web_utility.load_page(url)
    print(result[result.index('result'):])


def get_details(country_name):

    # country_name = str(country_name.title())
    input_file = open('currency_details.txt', mode='r', encoding='UTF-8')  # open file for reading

    for line in input_file:

        parts = line.strip().split(',')         #split into separate strings by removing ',' and white space at the end

        if parts[0] == country_name:
            input_file.close()
            return tuple(parts)

    input_file.close()
    return ()




details=get_details(input("Enter Country Name: "))
print(details)

# input_file = open('currency_details.txt', mode='r', encoding='UTF-8')
# print (input_file.readlines(6))
# input_file.close()