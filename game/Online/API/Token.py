# game packages
# graphics packages
from Graphics.Content.Text.WarningText import WarningText

# external packages
import requests


class Token:
    """
    Token for api calling

    parameters

    url : string
        the url for managing token
    """

    url = None
    token = None

    def __init__(self, url):
        self.url = url
        self.token = requests.get(f"{url}/api/generate-token").text

    def delete(self):
        requests.post(f"{self.url}/api/delete-token/{self.token}")

    def verify(self):
        if requests.get(f"{self.url}/api/verify-token/{self.token}").text == "False":
            WarningText("Couldn't verify token").display()
            self.delete()
            exit(0)
