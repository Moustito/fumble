import random

def dice_throw(sides):
    if sides <= 0:
        raise ValueError("Le nombre de faces doit être supérieur à 0.")
    return random.randrange(1, sides + 1)