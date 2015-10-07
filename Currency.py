import web_utility


input_file = open('currency_details.txt', mode = 'r')

def convert(amount, home_currency_code, location_currency_code):
    url= "https://www.google.com/finance/converter?a=1&from=AUD&to=JPY"
    result = web_utility.load_page(url_string)
    print(result[result.index('result'):])

def currency_details(country_name):
