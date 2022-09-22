# online game packages
from .Login import login

# graphics game packages
from Graphics.Content.Text.WarningText import WarningText

# external packages
import requests
import time


class API:
    """
    makes a class that handles all the api calls

    token: string
        token used for authenticating api calls
    """

    token = None
    url = None

    def __init__(self, token=None, url=None):
        self.token = token
        self.url = url

    def login(self, username, password):
        self.token.verify()
        try:
            return login(username, password, self.url)
        except:
            WarningText("Couldn't Log In...").display()
            time.sleep(3)
            self.token.delete()
            exit(0)
