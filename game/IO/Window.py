# built-in packages
import sys

# external packages
from rich.console import Console

console = Console()


def clear():
    for i in range(console.height):
        print("\n")

def enter_to_continue():
    input("press enter to continue...\n")

def move_to_top():
    for i in range(console.height - 3):
        print("")
