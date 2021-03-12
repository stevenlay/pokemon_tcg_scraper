from .Rule import Rule


class Card:
    def __init__(
        self, name, set_id, rarity, expansion_set, energy_type, card_img, rule=Rule.NONE
    ):
        self.__name = name
        self.__card_img = card_img
        self.__set_id = set_id
        self.__rarity = rarity
        self.__expansion_set = expansion_set
        self.__energy_type = energy_type
        self.__rule = rule

    def __str__(self):
        return (
            f"{self.__card_img}\n"
            f"{self.__name} - {self.__energy_type}\n"
            f"{self.__set_id} - {self.__rarity}\n"
            f"{self.__expansion_set}"
        )
