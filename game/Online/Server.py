# online game packages
from .API.API import API

# built-in packages
import requests

# graphics game content
from Graphics.Content.Text.WarningText import WarningText


class Server:
    url = None
    API = None

    def __init__(self, url="http://gdcheerios.com"):
        self.url = url
        try:
            requests.get(url)
        except:
            WarningText("Couldn't connect to server...").display()
            exit(1)
        self.API = API(requests.get(f"{url}/api/generate-token").text, url)
