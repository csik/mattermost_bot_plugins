"""!weather <place> returns a weather report from wttr for <place>"""
from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to

try:
    from urllib import quote
except ImportError:
    from urllib.request import quote

import requests


@respond_to('weather (.*)')
def wiki(message, searchterm):
    """return the top wiki search result for the term"""
    if not searchterm:
        searchterm = "funchal"
    searchterm = quote(searchterm)

    url = "http://wttr.in/"
    url = url.format(searchterm)

    result = requests.get(url)

    message.reply(u"{0}".format(result).encode('ascii', 'ignore'))
