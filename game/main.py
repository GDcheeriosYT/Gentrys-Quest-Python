# list of colors https://rich.readthedocs.io/en/stable/appendix/colors.html

# online packages
from rich.console import Console

# game packages
# online game packages
from Online.Server import Server
from Online.Account import AccountInfo
from Online.User import User
from Online.API import Login

# built-in packages
import sys
import time

# important variables
args = sys.argv
server = Server(args[3])
account_info = AccountInfo(args[1], args[2])
game_data = Login.login(account_info.username, account_info.password, server.url)
user = User(AccountInfo.username, game_data["inventory"])

# code
console = Console()
console.print("[blue bold underline]CARTER[white on orange1] [orange1 on white]BRAYDEN")
