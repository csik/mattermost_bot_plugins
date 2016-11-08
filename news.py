"""!wiki <topic> returns a wiki link for <topic>"""

from mattermost_bot.bot import listen_to
import logging
import feedparser

HELPTEXT = """
| cmd | publication |
| :------ | ----------:|
| tpm: | Talking Points Memo |
| pub: | Publico |
| gdn: | Guardian UK |
| nyt: | New York Times |
| hkn: | Hacker News (ycombinator) |
"""


def feed_url(name):
    return {
                'tpm': 'https://talkingpointsmemo.com/feed/all',
                'pub': 'http://feeds.feedburner.com/PublicoRSS',
                'gdn': 'https://www.theguardian.com/world/rss',
                'nyt': 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
                'hkn': 'https://news.ycombinator.com/rss',
                'help': HELPTEXT
            }.get(name, HELPTEXT)  # default if x not found


@listen_to('newz (.*)')
def newz_listen(message, searchterm):
    """Give news headlines from a variety of sources"""
    feed = feedparser.parse(feed_url(searchterm))
    return_val = ""
    for entry in feed.entries:
        return_val += str("[{0}]({1})\n".format(entry.title, entry.link))
    logging.info(return_val)
    message.reply(return_val)
    #message.reply("{}".format(str(return_val)))

    newz_listen.__doc__ = "Give news headlines from a variety of sources: newz nyt"
