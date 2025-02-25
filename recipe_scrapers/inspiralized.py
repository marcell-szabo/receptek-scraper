# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Inspiralized(AbstractScraper):
    @classmethod
    def host(cls):
        return "inspiralized.com"

    def title(self):
        return self.soup.find("h2").get_text()

    def author(self):
        if self.soup.find(string="Ali Maffucci"):
            return "Ali Maffucci"

    def total_time(self):
        return get_minutes(self.soup.find("span", {"itemprop": "totalTime"}))

    def yields(self):
        return get_yields(self.soup.find("span", {"itemprop": "servingSize"}))

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll("li", {"class": "instruction"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
