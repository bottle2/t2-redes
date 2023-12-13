"""Post messages to mitmproxy's event log."""
import logging
from mitmproxy import http

from mitmproxy.addonmanager import Loader
from mitmproxy.log import ALERT
from aux_info.src_images import images

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
        flow.request.url = images.get_random_image()
        logger.info(f"[righers] {flow.request.url}")


