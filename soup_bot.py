from bs4 import BeautifulSoup as bs
from pprint import pprint


class SoupScrap:
    def __init__(self, html_page):
        self.soup = bs(html_page, 'html.parser')

    def scrape(self):
        listings = self.soup.find_all(class_="property-card-data")
        # pprint(listings)
        entries = []
        for listing in listings:
            link = listing.find("a")['href']
            if link[0] != "h":
                link = "https://www.zillow.com" + link
            entry = {
                "address": listing.find("address").text,
                "price": listing.find("span").text.split(' ')[0],
                "link": link,
            }
            entries.append(entry)
        return entries
