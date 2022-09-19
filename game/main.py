# list of colors https://rich.readthedocs.io/en/stable/appendix/colors.html

# online packages
from rich.console import Console

# game packages
# online game packages
from Online.Server import Server
from Online.Account import AccountInfo
from Online.User import User
from Online.API import Login

# graphic game packages
from Graphics.Style import Style

# IO game packages
from IO import Window

# game data packages
import GameData

# built-in packages
import sys
import time

# important variables
args = sys.argv
server = Server(args[3])
account_info = AccountInfo(args[1], args[2])
game_data = GameData.GameData(Login.login(account_info.username, account_info.password, server.url))
user = User(account_info.username, game_data.generate_powerlevel())
console = Console()

# code
console.rule("Gentry's Quest")
console.print(f"Welcome {user.username}!")
console.status(f"Loading your data", spinner="dots").start()
time.sleep(2)
