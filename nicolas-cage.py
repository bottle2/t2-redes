"""Post messages to mitmproxy's event log."""
import logging
from mitmproxy import http

from mitmproxy.addonmanager import Loader
from mitmproxy.log import ALERT

logger = logging.getLogger(__name__)


def load(loader: Loader):
    logger.info("This is some informative text.")
    logger.warning("This is a warning.")
    #logger.error("This is an error.")
    logger.log(
        ALERT,
        "This is an alert. It has the same urgency as info, but will also pop up in the status bar.",
    )



"""Modify an HTTP form submission."""

def request(flow: http.HTTPFlow) -> None:
    logger.info(f"[poggers] {flow.request.url}")

    logger.info(flow.request.path)
    logger.info(type(flow.request.path))
    if ".jpg" in flow.request.url or ".png" in flow.request.url or ".webp" in flow.request.url or ".svg" in flow.request.url:
        flow.request.url = "https://img.olhardigital.com.br/wp-content/uploads/2023/05/super-homem-nicolas-cage.png"
        logger.info(f"[righers] {flow.request.url}")


