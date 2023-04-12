from bs4 import BeautifulSoup
import requests
import json # to save something in json file

with open("/home/helgenro/NSU_subjects/WEB_and_something/Parcer02/food_parcer/saved_web_page/index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

#1) We need to get all href from div
# class of the hrefs is ""

all_prod_hrefs = soup.find_all(class_ = "mzr-tc-group-item-href")

all_categorise_dict = {}
for item in all_prod_hrefs:

    item_text = item.text
    item_href = item.get("href")
    print(f"for {item_text} href is {item_href}")

    all_categorise_dict[item_text] = item_href

# Save to json file
with open("all_cat.json", "w") as file:
    json.dump(all_categorise_dict, file, indent=4, ensure_ascii=False)


# 2) We need to craete cicle for everuone page
#
count = 0
for cat_name, cat_href in all_categorise_dict:
    
    rep =[",", " ", "-", "'"]
    for item in rep:
        if item in cat_name:
            cat_name = cat_name.replace(item, "_")

    req = requests.get(url=cat_href, headers=headers)
    src = req.text
    with open() as file:
        file.write(src)

    count+=
