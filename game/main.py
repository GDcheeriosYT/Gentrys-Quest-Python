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
from Graphics.Text.Text import Text
from Graphics.Text.Text import Style

# Interface packages
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

# content packages
#from Content.Interfaces.Settings import

# IO game packages
from IO import Window

# game data packages
import GameData

# built-in packages
import sys
import time

# important variables
args = sys.argv[0]


console = Console()  # the console
Window.clear()  # clear window
print(args)
console.rule("Gentry's Quest")  #THE THINGGGGG

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

user = User(account_info.username, 99999, None)  # user class initialization
game_data = GameData.GameData(server.API.login(account_info.username, account_info.password))  # game data class initialization

# main code
in_game = True
while in_game:
    print("main menu")
    choices = int(input("1. play\n"
                    "2. settings\n"
                    "3. quit\n"))

    if choices == 1:
        print("now playing")
    elif choices == 2:
        print("now viewing settings")
    else:
        in_game = False

    Text(str(game_data.obtain().characters)).display()

server.API.token.delete()