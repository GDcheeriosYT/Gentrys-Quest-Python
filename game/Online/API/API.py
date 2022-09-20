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

    def verify_token(self):
        if requests.get(f"{self.url}/api/verify-token/{self.token}").text == "False":
            WarningText("Couldn't verify token").display()
            time.sleep(3)
            exit(0)

    def login(self, username, password):
        self.verify_token()
        try:
            return login(username, password, self.url)
        except:
            WarningText("Couldn't Log In...").display()
            time.sleep(3)
            exit(0)

