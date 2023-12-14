import logging
from mitmproxy import http

from mitmproxy.addonmanager import Loader
from mitmproxy.log import ALERT
from aux_info.src_images import images
import random

logger = logging.getLogger(__name__)

def is_image(accept):
    registries = [
        "application", "font", "example", "message", "model", "multipart", "text", "video"
    ]
    return "image" in accept and all(r not in accept for r in registries)

def request(flow: http.HTTPFlow) -> None:
    if "Accept" in flow.request.headers and is_image(flow.request.headers["Accept"]):
        flow.request.url = images.get_random_image_path()
