import logging

from app import all_books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = """Enter one of the options

- "b" to look at 5-star books
- "c" to look at cheapest books
- "n" to just get the next available book on the page
- "q" to exit

Enter your choice: """



def print_best_books(top = len(all_books)):
    """
    This function will return the best books by rating

    :param top: by default return the full list in order, but you can specify a range
    :return: None
    """
    logger.info('Finding best books by rating ...')
    best_books = sorted(all_books, key=lambda x: x.rating, reverse=True)[:top]
    for book in best_books:
        print(book)


def print_cheapest_books(top = len(all_books)):
    logger.info('Finding cheapest books books by price ...')
    cheap_books = sorted(all_books, key=lambda x: x.price)
    for book in cheap_books:
        print(book)

#Creating a generator and geting the next book
book_generator = (x for x in all_books)
def next_book():
    '''
    The generator can't be defined inside the function
    '''
    print(next(book_generator))


def menu():
    OPTIONS = {
        "b": print_best_books,
        "c": print_cheapest_books,
        "n": next_book
    }

    user_request = str(input(USER_CHOICE))
    while user_request != "q":
        if user_request not in OPTIONS.keys():
            print(f"{user_request} is not a valid option")
            user_request = str(input(USER_CHOICE))
        else:
            task = OPTIONS[user_request]
            task()
            user_request = str(input(USER_CHOICE))
    logger.debug("Terminating program.")


menu()


