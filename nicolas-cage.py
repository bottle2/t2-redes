import logging
from mitmproxy import http

from mitmproxy.addonmanager import Loader
from mitmproxy.log import ALERT

logger = logging.getLogger(__name__)

#badwords = open("badwords.txt", "r").get_value().split("\n")
#["addon", "method", "TCP", "request"]
image_types = [".jpg", ".png", ".webp", ".svg", ".ico", ".gif"]

#def load(loader: mitmproxy.addonmanager.Loader):
   
def done():
    dumper.close()

"""Modify an HTTP form submission."""
def request(flow: http.HTTPFlow) -> None:
    if any(i in flow.request.path for i in image_types):
        flow.request.url = "https://img.olhardigital.com.br/wp-content/uploads/2023/05/super-homem-nicolas-cage.png"

def response(flow: http.HTTPFlow) -> None:
    body = flow.response.get_text(False).lower()
#    for badword in badwords:
#        if badword in body:
            #flow.response.set_text(body.replace(badword, "noggers"))















#def load(loader: Loader):
#    logger.info("This is some informative text.")
#    logger.warning("This is a warning.")
#    #logger.error("This is an error.")
#    logger.log(
#        ALERT,
#        "This is an alert. It has the same urgency as info, but will also pop up in the status bar.",
#    )
