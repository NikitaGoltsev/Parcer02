from bs4 import BeautifulSoup
import requests
# despription - we need to get all product links and after
# that we will be able to get there "состав?"

#the link - "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

# Work with  url and requests lib
headers = { # That's to update
    
}

req = '' # the results of the requsts work