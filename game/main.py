# list of colors https://rich.readthedocs.io/en/stable/appendix/colors.html

# online packages
from rich.console import Console

# game packages
# online game packages
from Online.Server import Server
from Online.Account import AccountInfo
from Online.User.User import User

# graphic game packages
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Content.Text.InfoText import InfoText

# IO game packages
from IO import Window

# game data packages
import GameData

# built-in packages
import sys
import time

# important variables
args = sys.argv

"""
Initializing server connection info.

Incase of someone starting this without arguments we run through try and except blocks.
If a try bock finds an exception we'll use a default value.
"""

try:
    server = Server(args[3])  # make class to store server info
except IndexError:
    WarningText("No argument for server!\n").display()
    InfoText("Defaulting to https://gdcheerios.com\n").display()
    server = Server("https://gdcheerios.com")  # default server url
try:
    account_info = AccountInfo(args[1], args[2])  # make class to store account info
except IndexError:
    WarningText("No argument for account info!\n").display()
    InfoText("Program will now exit...")
    time.sleep(1)
    exit(1)

game_data = GameData.GameData(server.API.login(account_info.username, account_info.password))  # game data class initialization
user = User(account_info.username, 99999, None)  # user class initialization
console = Console()

# code
Window.clear()
console.rule("Gentry's Quest")
console.print(f"Welcome {user.username}!")
console.status(f"Loading your data", spinner="dots").start()
time.sleep(2)
