from bs4 import BeautifulSoup
import requests
import json # to save something in json file


with open('/home/helgenro/NSU_subjects/WEB_and_something/Parcer02/food_parcer/saved_web_page/index.html') as file:

    src = file.read()

soup = BeautifulSoup(src, "lxml")

all_links_dict = {}

all_prod_hrefs = soup.find_all(class_= "mzr-tc-group-item-href")
for item in all_prod_hrefs:
    #print(item.get("href"))
    item_name = item.text
    item_href = "https://health-diet.ru" + item.get("href")
    #             \-- add domaine name to find results

    all_links_dict[item_name] = item_href # to save in dictonary

for ct_name, ct_href in all_links_dict.items():
    rep = [',', ' ', '-', "'"]
    for item in rep:
        if item in ct_name:
            ct_name = ct_name.replace(item, "_")
    print(ct_name)

