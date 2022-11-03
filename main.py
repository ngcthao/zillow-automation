from soup_bot import SoupScrap
from selena_bot import SelenaBot
from pprint import pprint

selena_bot = SelenaBot()
html_page = selena_bot.get_html()

soup_bot = SoupScrap(html_page)
data = soup_bot.scrape()
# pprint(data)
selena_bot.input_fields(data=data)
