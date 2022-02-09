import re
import requests
from bs4 import BeautifulSoup


class PageCrawler:

    def __init__(self, url):
        self._url = url
        self._url_stamp = re.compile(r"https?://(?:[-\w.]|(%[\da-fA-F]{2}))+").match(self._url).group()

    def crawl(self, regex: str) -> list or None:
        """
        This method crawl on a specific website url and extract all it's mac address within it.
        :param regex:
        :return:
        """
        try:
            page = requests.get(self._url)
        except:
            print(f"The url {self._url} is not valid")
            return None

        matcher = re.compile(regex)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all(string=matcher)

        mac_address_list = []

        for entry in results:
            mac_address_list.append(matcher.search(entry.strip()).group())

        return mac_address_list

    def findNext(self) -> []:
        """
        Finds the url of the next page by scanning all the links in the page and finds the one
        that fits most by the characteristic of starting with the same url source and having the word
        page/start within it.
        :return: The next page url.
        """
        try:
            page = requests.get(self._url)
        except:
            print(f"The url {self._url} is not valid")
            return ""

        soup = BeautifulSoup(page.content, 'html.parser')
        urls = [item.get("href") for item in soup.find_all("a")]

        urls_final = list(dict.fromkeys(urls))
        urls_final = list(filter(None, urls_final))

        url_final = [x for x in urls_final if ("/" in x)]

        final_list = [self._url_stamp + s for s in urls_final]

        print(self._url, urls_final)

        return url_final
