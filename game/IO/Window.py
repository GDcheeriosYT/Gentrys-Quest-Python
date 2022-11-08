# built-in packages
import sys

# external packages
from rich.console import Console

console = Console()


def clear():
    for i in range(console.height):
        print("\n")


def move_to_top():
    for i in range(console.height - 3):
        print("")


def place_rule(text):
    console.rule(text)
