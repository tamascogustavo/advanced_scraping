# -*- coding: utf-8 -*-
# @Author: gustavotamascohotmail.com
# @Date:   2022-02-28 13:10:11
# @Last Modified by:   gustavotamascohotmail.com
# @Last Modified time: 2022-02-28 13:10:11
import re
import logging

from locators.book_locator import BookLocator

logger = logging.getLogger('scraping.books')

class ParseBook:

    RATING = {
        "ONE": 1,
        "TWO": 2,
        "THREE": 3,
        "FOUR": 4,
        "FIVE": 5
    }

    def __init__(self, parent):
        logger.debug(f"New book parser created from `{parent}`")
        self.parent = parent

    def __repr__(self):
        return f"<The book {self.name} has {self.rating} stars and costs {self.price}>"

    @property
    def name(self):
        logger.debug("Finding book name ...")
        locator = BookLocator.NAME_LOCATOR
        name = self.parent.select_one(locator).attrs["title"]
        logger.debug(f"Found book name {name}")
        return name

    @property
    def link(self):
        logger.debug("Finding book link ...")
        locator = BookLocator.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs["href"]
        logger.debug(f"Found book link: `{item_link}`")
        return item_link

    @property
    def price(self):
        logger.debug("Finding book price ...")
        locator = BookLocator.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        pattern = "([0-9]+\.[0-9]+)"
        price_obj = re.search(pattern, item_price)
        price = float(price_obj[0])
        logger.debug(f"Found book price: `{price}`")
        return price

    @property
    def rating(self):
        logger.debug("Finding book rating ...")
        locator = BookLocator.RATING_LOCATOR
        info = self.parent.select_one(locator)
        classes = info.attrs["class"]
        rating_class = [x for x in classes if x != "star-rating"]
        rating = "".join(rating_class).upper()
        rate = ParseBook.RATING.get(rating)
        logger.debug(f"Found book rate: `{rate}`")
        return rate





