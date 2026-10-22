import random

def dice(n):
    if n <= 0:
        raise ValueError("Le nombre de faces doit être supérieur à 0.")
    return random.randrange(1, n + 1)