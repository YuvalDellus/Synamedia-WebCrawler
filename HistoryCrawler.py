class HistoryCrawler:

    def __init__(self, pages_to_scan: list):
        self._pages_to_scan = iter(pages_to_scan)
        self._pages_to_scan_list = pages_to_scan
        self._pages_scanned = []
        self._pages_to_add = []

    def _update_list(self) -> None:
        """
        Updates the urls pending list once it got empty and the user added manually more address.
        """
        self._pages_to_scan = iter(self._pages_to_add.copy())
        self._pages_to_scan_list = self._pages_to_add.copy()
        self._pages_to_add = []

    def add(self, url: str) -> None:
        """
        Adds a new url to the crawler pending list
        :param url: string that represents the new url.
        """
        conditions = [url in self._pages_scanned, url in self._pages_to_add, url in self._pages_to_scan_list]
        if any(conditions):
            pass  # the url already been crawled or pending to be crawl
        else:
            self._pages_to_add.append(url)

    def next(self) -> str:
        """
        Iterate over the pending list and return the next url in line.
        If list is empty, checks if user added manually more urls and act accordingly.
        :return: next url address to crawl on.
        """
        try:
            next_url = self._pages_to_scan.__next__()
        except:
            if self._pages_to_add:
                self._update_list()
                next_url = self._pages_to_scan.__next__()
            else:
                return "-1"

        self._pages_scanned.append(next_url)

        return next_url
