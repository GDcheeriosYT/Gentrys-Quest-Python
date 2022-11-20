# online game packages
from .Login import login
from .UploadData import upload_data

# graphics game packages
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Content.Text.InfoText import InfoText

# external packages
import time


class API:
    """
    makes a class that handles all the api calls

    token: string
        token used for authenticating api calls
    """

    token = None
    url = None
    id = None

    def __init__(self, token=None, url=None, id=None):
        self.token = token
        self.url = url
        self.id = id

    def login(self, username, password):
        self.token.verify()
        login_result = login(username, password, self.url)
        if login_result == "nope":
            WarningText("Couldn't Log In...").display()
            time.sleep(1)
            self.token.delete()
            exit(0)
        else:
            self.id = login_result["id"]
            return login_result

    def upload_data(self, data):
        upload_data(self.url, self.id, data, self.token.token)