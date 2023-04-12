from bs4 import BeautifulSoup
import requests
import json # to save something in json file

from for_food_prc import headers

with open("/home/helgenro/NSU_subjects/WEB_and_something/Parcer02/food_parcer/saved_web_page/index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

#1) We need to get all href from div
# class of the hrefs is ""

all_prod_hrefs = soup.find_all(class_ = "mzr-tc-group-item-href")

all_categorise_dict = {}
for item in all_prod_hrefs:

    item_text = item.text
    item_href = "https://health-diet.ru" + item.get("href")
    #print(f"for {item_text} href is {item_href}")

    all_categorise_dict[item_text] = item_href

# Save to json file
#with open("all_cat.json", "w") as file:
    #json.dump(all_categorise_dict, file, indent=4, ensure_ascii=False)
with open("all_cat.json") as file:
    all_categorise = json.load(file)

# 2) We need to craete cicle for everuone page
#
count = 0
for cat_name, cat_href in all_categorise.items():
    
    if count == 0: # That's to work only with one category for the first time
        rep =[",", " ", "-", "'"]
        for item in rep:
            if item in cat_name:
                cat_name = cat_name.replace(item, "_")

        #req = requests.get(url=cat_href)
        #src = req.text

        #with open("write_cd.html", "w") as file:
            #file.write(src)

        with open("write_cd.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        #Let's get headers of the table
        tabl_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
        #print(tabl_head)
    count += 1
