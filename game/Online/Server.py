# online game packages
from .API.API import API

# built-in packages
import requests


class Server:
    url = None
    API = None

    def __init__(self, url="http://gdcheerios.com"):
        self.url = url
        self.API = API(requests.get(f"{url}/api/generate-token").text, url)
