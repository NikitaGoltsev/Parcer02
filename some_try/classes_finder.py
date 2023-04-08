from bs4 import BeautifulSoup

#soup define some bs4 object
#soup = ...

with open("/home/helgenro/NSU_subjects/WEB_and_something/Parcer02/some_try/html_file/index.html") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")
# print(src) # the src is a bs4 object

# class finder
user_name = soup.find("div", class_="user__name")
print(user_name)