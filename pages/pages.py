# -*- coding: utf-8 -*-
# @Author: gustavotamascohotmail.com
# @Date:   2022-02-28 13:10:27
# @Last Modified by:   gustavotamascohotmail.com
# @Last Modified time: 2022-02-28 13:10:27

import logging

from bs4 import BeautifulSoup
from locators.page_locator import PageLocator
from books.books import ParseBook

logger = logging.getLogger('scraping.pages')

class PagesParser:
    def __init__(self, page_content):
        logger.debug("Parsing page contente with BS4 HTML parser")
        self.soup = BeautifulSoup(page_content, "html.parser")

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{PageLocator.PAGE}`')
        locator = PageLocator.PAGE
        all_books = self.soup.select(locator)
        return [ParseBook(book) for book in all_books]

    @property
    def page_count(self):
        logger.debug(f'Finding page count in the page using `{PageLocator.COUNTER}`')
        content = self.soup.select_one(PageLocator.COUNTER).string
        number_of_pages = int(content.split()[-1])
        logger.debug(f'Extracted number of pages as integer: `{number_of_pages}`')
        return number_of_pages




