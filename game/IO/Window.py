# built-in packages
import sys

# external packages
from rich.console import Console

console = Console()


def clear():
    sys.stdout.flush()


def move_to_top():
    for i in range(console.height - 3):
        print("")
