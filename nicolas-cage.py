import logging
from mitmproxy import http

from mitmproxy.addonmanager import Loader
from mitmproxy.log import ALERT
from mitmproxy import command
from aux_info.src_images import ImageList
from aux_info.src_images import Image
import random

logger = logging.getLogger(__name__)

images = ImageList()

def is_image(accept):
    registries = [
        "application", "font", "example", "message", "model", "multipart", "text", "video"
    ]
    return "image" in accept and all(r not in accept for r in registries)

def request(flow: http.HTTPFlow) -> None:
    if "Accept" in flow.request.headers and is_image(flow.request.headers["Accept"]):
        flow.request.url = images.get_random_image_path()

class nicolas:
    @command.command("nicolas.list")
    def print(self):
        logger.info(f"Got {len(images.images)} images")
        images.print_images(logger)

    @command.command("nicolas.set")
    def set(self, name : str, url : str):
        images.add_image(Image(name, url))

    @command.command("nicolas.del")
    def dele(self, name : str):
        images.remove_image(name)

addons = [nicolas()]
