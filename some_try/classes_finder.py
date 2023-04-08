from bs4 import BeautifulSoup

with open("html_file/index.html") as file:
    src = file.read()

print(src)