import random

random_character_names = [
    "pooper man"
]

random_weapon_names = [
    "The Meow"
]
def get_random_name(character_name=True):
    if character_name:
        return random.choice(random_character_names)
    else:
        return random.choice(random_weapon_names)
