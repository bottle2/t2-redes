import logging
from mitmproxy import http

from mitmproxy.addonmanager import Loader
from mitmproxy.log import ALERT
from aux_info.src_images import images
from badwords import manager
import random

logger = logging.getLogger(__name__)

le_manager = manager()
#["addon", "method", "TCP", "request"]
image_types = [".jpg", ".png", ".webp", ".svg", ".ico", ".gif"]

"""Modify an HTTP form submission."""
def request(flow: http.HTTPFlow) -> None:
    if any(i in flow.request.path for i in image_types):
        flow.request.url = images.get_random_image()

def response(flow: http.HTTPFlow) -> None:
    body = flow.response.get_text(False).lower()
    #if "Content-Type" in  flow.response.headers and "html" in flow.response.headers["Content-Type"]:

    logger.info(flow.response.headers["Content-Type"])
    #with open("penis.txt", "a") as file:
    #    file.write(flow.request.pretty_host)
    #    file.write(flow.response.get_text(False))
    for badword in le_manager.badwords:
        goodword = random.choice(le_manager.goodwords)
        body = body.replace(' ' + badword.lower() + ' ', ' ' + goodword + ' ')
        body = body.replace(' ' + badword.lower() + ',', ' ' + goodword + ',')
        body = body.replace(' ' + badword.lower() + '.', ' ' + goodword + '.')
        body = body.replace(' ' + badword.lower() + '!', ' ' + goodword + '!')
        body = body.replace(' ' + badword.lower() + '?', ' ' + goodword + '?')
        body = body.replace(' ' + badword.lower() + ':', ' ' + goodword + ':')
    flow.response.set_text(body)

    #logger.info(f"there are {len(le_manager.badwords)} badwords and {len(le_manager.goodwords)}")
        #    if badword.lower() in body:
        #        flow.response.set_text(body.replace(badword.lower(), random.choice(le_manager.goodwords)))















#def load(loader: Loader):
#    logger.info("This is some informative text.")
#    logger.warning("This is a warning.")
#    #logger.error("This is an error.")
#    logger.log(
#        ALERT,
#        "This is an alert. It has the same urgency as info, but will also pop up in the status bar.",
#    )
