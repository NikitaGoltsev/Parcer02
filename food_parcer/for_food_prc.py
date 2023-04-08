from bs4 import BeautifulSoup
import requests
# despription - we need to get all product links and after
# that we will be able to get there "состав?"

#the link - "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

# Work with  url and requests lib
headers = { # That's to update user agents, to show web page - we are not bots
    "Accept" : "*/*",
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    # That's parametrs to get acces for cite information
    # We are able to check them into web page
    # Also there are some libs to generate them ?
}

req = requests.get(url, headers=headers)
src = req.text
#print(req)

with open("index.html", "w") as file:
    file.write(src) # To not be banned with to much acces from one device 