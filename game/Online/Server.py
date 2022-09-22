# online game packages
from .API.API import API
from .API.Token import Token

# built-in packages
import requests

# graphics game content
from Graphics.Content.Text.WarningText import WarningText


class Server:
    url = None
    API = None

    def __init__(self, url="https://gdcheerios.com"):
        self.url = url
        try:
            requests.get(url)
        except:
            WarningText("Couldn't connect to server...").display()
            exit(1)
        self.API = API(Token(url), self.url)
