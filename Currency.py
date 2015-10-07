import web_utility

def convert(amount, home_currency_code, location_currency_code):
    url= str("https://www.google.com/finance/converter?a=" + str(amount) +"&from=" + home_currency_code + "&to=" + location_currency_code )
    result = web_utility.load_page(url)
    print(result[result.index('result'):])

def currency_details(country_name):
    country_name.capitalize
    input_file = open('currency_details.txt', mode = 'r', encoding= 'UTF-8') #open file for reading
    line = currency_details.readline()

    while country_name not in line:
                currency_details

   readline ()
   input_file = close('currency_details.txt', )


country_name = input("Enter Country Name: ")



