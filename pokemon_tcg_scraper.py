import requests as r
from constants import *
from bs4 import BeautifulSoup as bs
from models.Card import Card


if __name__ == "__main__":
    for i in range(100, 121):
        num = str(i)
        url = f"{BASE_URL}/ss-series/swsh45sv/SV{num.zfill(3)}/"
        page = r.get(url)
        soup = bs(page.content, "html.parser")

        # Get Card Image
        cardItem = soup.find(attrs={"class": "card-image"})
        card_img = cardItem.img["src"]
        # print(card_img)

        # Get Card Details
        card_details = soup.find("div", attrs={"class": "card-description"})
        card_name = card_details.h1.text
        card_energy = card_details.i["class"][1].split("-")[1]

        # Get Card Expansion Info
        card_stats = soup.find("div", attrs={"class": "stats-footer"})
        card_expansion = card_stats.h3.text
        card_set, card_rarity = card_stats.span.text.split(" ", 1)

        pokemon = Card(
            card_name, card_set, card_rarity, card_expansion, card_energy, card_img
        )
