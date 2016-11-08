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


#@respond_to('weather (.*)')
#def weather(message, searchterm):
#    """return the weather search result for the term"""
#    logging.info('before curl')
#    cmd = [ 'curl','http://wttr.in/funchal']
#    output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
#    t = output.decode()
#    t = t.split('┌─────────────┐')
#    t[3]=t[3].split('\n\n')[0]
#    keys = ('now', 'today', 'tomorrow', 'later')
#    weather = dict(zip(keys,t))
#    logging.warning(weather.get(searchterm))
#    message.reply("``\n{0}\n``".format(str(weather.get(searchterm))))
#
#test22 = """
#``
#    \  /       Partly cloudy
#  _ /"".-.     21 °C          
#    \_(   ).   ↓ 0 km/h       
#    /(___(__)  10 km          
#               0.2 mm   
#``
#"""
#
#@listen_to('wea_wea')
#def wea_wea(message):
#    message.comment(test22)
#
#@respond_to('ww')
#def weather(message):
#    import pycurl
#    from io import BytesIO
#    
#    buffer = BytesIO()
#    c = pycurl.Curl()
#    c.setopt(c.URL, 'http://wttr.in/funchal')
#    c.setopt(c.WRITEDATA, buffer)
#    c.perform()
#    c.close()
#     
#    body = buffer.getvalue()
#    output = body.decode('iso-8859-1')
#    #logging.warning(body)
#    logging.warning(str(body))
#    #logging.warning(output)
#    logging.warning('About to try message.comment')
#    # Body is a byte string.
#    # We have to know the encoding in order to print it to a text file
#    # such as standard output.
#    message.comment(output)
#    logging.warning('tried message.comment')
#
