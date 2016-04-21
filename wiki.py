"""!wiki <topic> returns a wiki link for <topic>"""
import re

from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to

try:
   from urllib import quote
except ImportError:
    from urllib.request import quote

import requests
from bs4 import BeautifulSoup


@respond_to('wiki (.*)')
def wiki(message, searchterm):
    """return the top wiki search result for the term"""
    searchterm = quote(searchterm)

    url = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={0}&format=json"
    url = url.format(searchterm)

    result = requests.get(url).json()

    pages = result["query"]["search"]

    # try to reject disambiguation pages
    pages = [p for p in pages if 'may refer to' not in p["snippet"]]

    if not pages:
        return ""

    page = quote(pages[0]["title"].encode("utf8"))
    link = "http://en.wikipedia.org/wiki/{0}".format(page)

    r = requests.get("http://en.wikipedia.org/w/api.php?format=json&action=parse&page={0}".format(page)).json()
    soup = BeautifulSoup(r["parse"]["text"]["*"], "html5lib")
    p = soup.findAll('p')
    for i in p:
        if i.find('b'):
            p = i.get_text()
            break
    
    message.reply(u"{0}\n{1}".format(p, link).encode('ascii', 'ignore'))
