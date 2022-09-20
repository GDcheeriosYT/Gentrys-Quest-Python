# list of colors https://rich.readthedocs.io/en/stable/appendix/colors.html

# online packages
from rich.console import Console

# game packages
# online game packages
from Online.Server import Server
from Online.Account import AccountInfo
from Online.User.User import User

# graphic game packages

# IO game packages
from IO import Window

# game data packages
import GameData

# built-in packages
import sys
import time

# important variables
args = sys.argv
server = Server(args[3], )
account_info = AccountInfo(args[1], args[2])
game_data = GameData.GameData(server.API.login(account_info.username, account_info.password))
user = User(account_info.username, 99999, None)
console = Console()

# code
Window.clear()
console.rule("Gentry's Quest")
console.print(f"Welcome {user.username}!")
console.status(f"Loading your data", spinner="dots").start()
time.sleep(2)
