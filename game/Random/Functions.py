import random

random_character_names = [
    "pooper man"
]

random_item_names = [
    "The Meow",
    "kfc fries",
    "lucas's iphone"
]


def get_random_name(character_name=True):
    if character_name:
        return random.choice(random_character_names)
    else:
        return random.choice(random_item_names)


def determine_crit(crit_rate):
    if random.uniform(0, 100) < crit_rate:
        return True
    else:
        return False


def generate_artifact_star_rating(difficulty):
    # generate a star rating
    return difficulty
