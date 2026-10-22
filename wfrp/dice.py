import random

def dice_throw(sides: int) -> int:
    if isinstance(sides, bool) or not isinstance(sides, int):
            raise TypeError("Le nombre de faces doit être un chiffre.")
    if sides <= 0:
            raise ValueError("Le nombre de faces doit être supérieur à 0.")
    return random.randrange(1, sides + 1)