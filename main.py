import WebsiteCrawler

if __name__ == '__main__':
    url = "https://global-satinfo.in/viewtopic.php?t=708"
    # more_urls = [
    #     "https://www.smarttechvillas.com/new-stalker-iptv-codes-portal-url-and-mac-address-for-nov-2021/",
    #     "https://webloadedtech.com/ott-navigator-free-iptv-login-and-mac-address/",
    #     "https://spacetriptv.com/iptv-macaddress-generator/",
    #     "https://www.tapuz.co.il/threads/img-http-timg-co-il-f-emo77-gif-img-%D7%94%D7%99%D7%9C%D7%93-%D7%A9%D7%9C%D7%9B%D7%9D-%D7%97%D7%95%D7%92%D7%92-%D7%99%D7%95%D7%9E%D7%95%D7%9C%D7%93%D7%AA-%D7%95%D7%90%D7%A0%D7%97%D7%A0%D7%95-%D7%9E%D7%90%D7%A8%D7%92%D7%A0%D7%99%D7%9D-%D7%9C%D7%95-%D7%9E%D7%A1%D7%99%D7%91%D7%94-%D7%A7%D7%A1%D7%95%D7%9E%D7%94-img-http-timg-co-il-f-emo70-gif-img.14921818/"
    # ]

    url = "https://alliptvurl.blogspot.com/"

    crawler = WebsiteCrawler.WebsiteCrawler(url, 3)

    # for i in more_urls:
    #     crawler.add(i)

    crawler.run()
