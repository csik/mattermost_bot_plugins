"""!image <search term> return a random result from the google image search result for <search term>"""

try:
    from urllib import quote
except ImportError:
    from urllib.request import quote
import re
import requests
from random import shuffle

from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to

def unescape(url):
    # for unclear reasons, google replaces url escapes with \x escapes
    return url.replace(r"\x", "%")

@respond_to('image (.*)')
def image(message, searchterm):
    searchterm = quote(searchterm)

    safe = "&safe=active"
    searchurl = "https://www.google.com/search?tbm=isch&q={0}{1}".format(searchterm, safe)

    # this is an old iphone user agent. Seems to make google return good results.
    useragent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Versio  n/4.0.5 Mobile/8A293 Safari/6531.22.7"

    result = requests.get(searchurl, headers={"User-agent": useragent}).text

    images = list(map(unescape, re.findall(r"var u='(.*?)'", result)))
    shuffle(images)

    if images:
        message.reply( images[0])
    else:
        message.reply( "")


