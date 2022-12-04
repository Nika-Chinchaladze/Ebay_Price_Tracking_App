import requests
from bs4 import BeautifulSoup
from Available_Info import AddressLinks


class EbayPrice:
    def __init__(self):
        self.help_tool = AddressLinks()
        self.my_header = {
            "Accept-Language": self.help_tool.Language,
            "User-Agent": self.help_tool.User_Agent
        }

    def get_current_price(self, product_link):
        respond = requests.get(url=product_link, headers=self.my_header)
        website = respond.text
        soup = BeautifulSoup(website, "html.parser")
        df = f"{soup.find(name='div', class_='x-price-primary')}"
        starting = df.find("$")
        first_price = df[starting+1:]
        ending = first_price.find("<")
        price = first_price[:ending]
        if "," in price:
            price = price.replace(",", "")
        else:
            pass
        return price

