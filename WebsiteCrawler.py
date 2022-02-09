import PageCrawler
import HistoryCrawler
from random import randint
from time import sleep


def nextPageCalculator(url: str) -> (int, int):
    """
    Some websites needs different jumps from one page to another (ex, start=10->start=20 or page=1->page=2),
    This function extract the differ, evaluate it and returns the differ and it's len.
    :param url: the url of the next page to evaluate.
    :return: the differ and it's len.
    """
    suffix = ""
    for letter in reversed(url):
        if not letter.isnumeric():
            break
        suffix += letter

    suffix = suffix[::-1]
    suffix = ""

    return int(suffix), len(suffix)


class WebsiteCrawler:

    def __init__(self, url: str, max_pages_to_crawl: int):
        self._regex = r"\b([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}"
        self._url = url
        self._max_pages_to_crawl = max_pages_to_crawl
        self._history_crawler = HistoryCrawler.HistoryCrawler([url])
        self._page_crawler = PageCrawler

    # def run(self) -> None:
    #     """
    #     Start the crawling process on all the given urls, if a website came with request for several pages, the method
    #     will evaluate the url attached and add the next pages url to the history crawler to pend.
    #     """
    #     page_address = self._history_crawler.next()
    #     count = 1
    #     next_page_url_start = ""
    #
    #     while page_address != "-1":
    #         # please comment next line on/off for better run times ----------------
    #         # sleep(randint(1, 2))  # avoiding IP address from being banned
    #
    #         next_page_scalar = 0
    #         curr_crawler = self._page_crawler.PageCrawler(page_address)
    #
    #         print(page_address)
    #         print("The mac addresses found in this page are: ")
    #         print(curr_crawler.crawl(self._regex))
    #
    #
    #         while self._max_pages_to_crawl - count:
    #
    #             if not next_page_scalar:
    #                 next_page_url = curr_crawler.findNext()
    #
    #                 if not next_page_url:
    #                     print("next page not found")
    #                     count = self._max_pages_to_crawl
    #                     break
    #
    #                 if next_page_url[0] == "/":
    #                     next_page_url = next_page_url_start[1:]
    #
    #                 next_page_scalar, suffix_len = nextPageCalculator(next_page_url)
    #
    #                 next_page_url_start = next_page_url[0:-suffix_len]  # www.../page-2 -> www.../page-
    #
    #             next_page_url = next_page_url_start + str(next_page_scalar * count)
    #             self._history_crawler.add(next_page_url)
    #             count += 1
    #
    #         page_address = self._history_crawler.next()
    #
    #     print("\nNo more pages to crawl")

    def run(self) -> None:
        """
        Start the crawling process on all the given urls, if a website came with request for several pages, the method
        will evaluate the url attached and add the next pages url to the history crawler to pend.
        """
        page_address = self._history_crawler.next()
        count = 1
        next_page_url_start = ""

        while page_address != "-1":
            # please comment next line on/off for better run times ----------------
            # sleep(randint(1, 2))  # avoiding IP address from being banned

            next_page_scalar = 0
            curr_crawler = self._page_crawler.PageCrawler(page_address)

            print(page_address)
            print("The mac addresses found in this page are: ")
            print(curr_crawler.crawl(self._regex))

            next_pages = []
            if count > 1:
                next_pages = curr_crawler.findNext()
                for page in next_pages:
                    self._history_crawler.add(page)


            while self._max_pages_to_crawl - count:
                next_pages.append(curr_crawler.findNext())
                # if not next_page_scalar:
                #     next_page_url = curr_crawler.findNext()

                # if not next_page_url:
                #     print("next page not found")
                #     count = self._max_pages_to_crawl
                #     break

                # if next_page_url[0] == "/":
                #     next_page_url = next_page_url_start[1:]

                # next_page_scalar, suffix_len = nextPageCalculator(next_page_url)

                # next_page_url_start = next_page_url[0:-suffix_len]  # www.../page-2 -> www.../page-

            next_page_url = next_page_url_start + str(next_page_scalar * count)
            self._history_crawler.add(next_page_url)
            count += 1

        page_address = self._history_crawler.next()

    print("\nNo more pages to crawl")


def add(self, url: str) -> None:
    """
    Adds an url to crawl on to the history crawler
    """
    self._history_crawler.add(url)
