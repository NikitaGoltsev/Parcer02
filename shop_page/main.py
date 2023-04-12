import bs4 as BeutifulSoap
import requests


class Page_Worker():

    url = "https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/"
    headers = {
        "Accept":"",
        "User-Agent":""
    }

    def __init__(self) -> None:
        pass

    def write_to_html(self) -> None:

        req = requests.get(self.url)
        src = req.text
        with open("index.html",  "w") as file:
            file.write(src)

        return None
    
    def __open_and_save__(self) -> None:

        with open("index.html") as file:
            src = file.read()
        
        self.soup = BeutifulSoap(src, "lxml")

        return None
    
    def get_headera_and_href(self):
