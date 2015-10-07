import web_utility

def convert(amount, home_currency_code, location_currency_code):
    url= str("https://www.google.com/finance/converter?a='str(amount)'&from='home_currency_code'&to='location_currency_code'")
    result = web_utility.load_page(url_string)
    print(result[result.index('result'):])

def currency_details(country_name):


   input_file = open('currency_details.txt', mode = 'r', encoding= 'UTF-8')


convert(1, 'AUD', 'USD')

