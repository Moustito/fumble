


def dice_in_array(dice: int, table: tuple):
    '''Using a die and an array, it returns the value form the array that corresponds to the value of the die'''
    for entry, label in table:
        # Si c'est un tuple, c'est une tranche (min, max)
        if isinstance(entry, tuple):
            start, end = entry
            if start <= dice <= end:
                return label
        # Sinon, c'est une valeur unique exacte
        else:
            if entry == dice:
                return label
    raise ValueError(f"Le nombre {dice} ne correspond à aucune tranche.")
