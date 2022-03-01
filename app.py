# -*- coding: utf-8 -*-
# @Author: gustavotamascohotmail.com
# @Date:   2022-02-28 13:08:53
# @Last Modified by:   gustavotamascohotmail.com
# @Last Modified time: 2022-02-28 13:12:46

import requests
import logging

from pages.pages import PagesParser

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='log.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

"""
This is to scrape the first page with a different link
"""

page_content = requests.get("http://books.toscrape.com").content
page = PagesParser(page_content)
all_books = page.books

"""
To scrape all the others
"""
for n_p in range(1,page.page_count):
    link = f"http://books.toscrape.com/catalogue/page-{n_p+1}.html"

    #Get the content of the web page
    page_content = requests.get(str(link)).content

    #Parse the html info of each book
    page = PagesParser(page_content)

    #Create a list of book objects parsed
    all_books.extend(page.books)


