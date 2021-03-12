import requests as r
from constants import *
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
from models.Card import Card


if __name__ == "__main__":
    cards = []
    for i in range(1, 123):
        num = str(i)
        url = f"{BASE_URL}/ss-series/swsh4/{num}/"
        page = r.get(url)
        soup = bs(page.content, "html.parser")

        # Get Card Image
        cardItem = soup.find(attrs={"class": "card-image"})
        card_img = cardItem.img["src"]

        # Get Card Details
        card_details = soup.find("div", attrs={"class": "card-description"})
        card_name = card_details.h1.text
        card_category = card_details.h2.text
        if "Trainer" not in card_category:
            card_type = card_details.i["class"][1].split("-")[1]
        else:
            card_type = card_category

        # Get Card Expansion Info
        card_stats = soup.find("div", attrs={"class": "stats-footer"})
        card_expansion = card_stats.h3.text
        card_set, card_rarity = card_stats.span.text.split(" ", 1)

        cards.append(
            [card_name, card_set, card_rarity, card_expansion, card_type, card_img]
        )

    # print(cards)

    column_names = ["name", "set", "rarity", "expansion", "type", "img"]
    df = pd.DataFrame(cards, columns=column_names)
    # print(df)
    df.to_json(path_or_buf="data/output_vv.json", orient="records")
