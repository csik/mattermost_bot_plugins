"""!weather <place> returns a weather report from wttr for <place>"""
from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to
import subprocess
import logging
import html2text
import requests

@respond_to('wet (.*)')
def wet(message, searchterm):
   r = requests.get('http://wttr.in/funchal')
   h = html2text.HTML2Text()
   t = str(h.handle(r.text))
   t = t.split('┌─────────────┐')
   t[3]=t[3].split('\n\n')[0]
   keys = ('now', 'today', 'tomorrow', 'later')
   weather = dict(zip(keys,t))
   logging.info(weather.get(searchterm))
   message.reply("""
``
{0}
``
""".format(weather.get(searchterm)))

wet.__doc__ = "Get weather for today or tomorrow: @mitibot wet today"
