from bs4 import BeautifulSoup

#soup define some bs4 object
#soup = ...

with open("/home/helgenro/NSU_subjects/WEB_and_something/Parcer02/some_try/html_file/index.html") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")
# print(src) # the src is a bs4 object

# class finder
user_name = soup.find("div", class_="user__name")
# print(user_name.text)
#                \ text method
# There are three ways to find somthing
# 1) simple find 
user_name = soup.find("div", class_="user__name").text
# 2) with dictionary
user_name_02 = soup.find("div", {"class" : "user__name"}).find("span").text
# 3) find all
# In exampl i would like to find all lincs from li tag
# After check I see, all that links are in class "social_networks"

links_finder = soup.find("div", {"class" : "user__info"}).find("div",
    {"class" : "social__networks"}).find_all("a")

for i in range(len(links_finder)):
    print(f"links num:{i+1} is {links_finder[i]}")


# The method get - is to get something from atribute
# let's moder our for cicle
for item in links_finder:
    item_txt = item.text
    item_url = item.get("href")
    print(f"the link on the {item_txt} is {item_url}")


# also the are other method to move by the structer 

# .find_parantes
# .find_kids

# other methods
# .next_elem - move on one step ( or find.next() )