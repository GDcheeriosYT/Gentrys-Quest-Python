# list of colors https://rich.readthedocs.io/en/stable/appendix/colors.html

# online packages
from rich.console import Console

# game packages
from GameData import GameData
from Game import Game

# online game packages
from Online.Server import Server
from Online.Account import AccountInfo
from Online.User.User import User

# graphic game packages
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Content.Text.InfoText import InfoText

# testing packages
from testing.TestingHandler import TestingHandler

# IO game packages
from IO import Window

# built-in packages
import sys
import time

# important variables
args = sys.argv
debug_mode = False
if len(args) > 1:
    debug_mode = False
else:
    debug_mode = True

console = Console()  # the console
Window.clear()  # clear window

"""
Initializing server connection info.

Incase of someone starting this without arguments we run through try and except blocks.
If a try bock finds an exception we'll use a default value.
"""

if debug_mode:
    console.rule("Gentry's Quest [DEBUG MODE]")
    TestingHandler().start()
else:
    console.rule("Gentry's Quest")
    try:
        server = Server(args[3])  # make class to store server info
    except IndexError:
        WarningText("No argument for server!\n").display()
        InfoText("Defaulting to https://gdcheerios.com\n").display()
        server = Server("https://gdcheerios.com")  # default server url
    try:
        account_info = AccountInfo(args[1], args[2])  # make class to store account info
        user = User(account_info.username, 99999, None)  # user class initialization
        user_data = server.API.login(account_info.username, account_info.password)  # game data class initialization
        game_data = GameData(user_data["metadata"]["Gentry's Quest data"])
    except IndexError:
        WarningText("No argument for account info!\n").display()
        InfoText("Program will now exit...")
        time.sleep(1)
        exit(1)
    game = Game(game_data)
    game.start()

    server.API.upload_data(game.game_data)
    server.API.token.delete()
