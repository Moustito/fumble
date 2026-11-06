def dice_in_array(dice: int, table: tuple):
    '''Pour un jet et une table de plages, renvoie l’entrée correspondante.'''
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


def validate_table(table):
    '''Valide les table de 1 à 100 sans chevauchement et trou.'''
    intervals = []

    # 1. Normalisation : on transforme tout en (start, end)
    for entry, label in table:
        if isinstance(entry, tuple):
            start, end = entry
        else:
            start = end = entry
        intervals.append((start, end))
        
    # 2. Tri des intervalles par leur valeur de début
    intervals.sort(key=lambda x: x[0])

    # 3. Vérification de la règle 1 : le premier commence à 1
    if intervals[0][0] != 1:
        raise ValueError("La table doit commencer à 1.")

    # 4. Vérification de la règle 2 : le dernier finit à 100
    if intervals[-1][1] != 100:
        raise ValueError("La table doit terminer à 100.")

    # 5. Vérification des trous et chevauchements entre les morceaux
    for i in range(len(intervals) - 1):
        current_end = intervals[i][1]
        next_start = intervals[i+1][0]
        
        # Le début du suivant doit être exactement la fin du courant + 1
        if next_start != current_end + 1:
            raise ValueError(f"Trou ou chevauchement détecté entre {intervals[i]} et {intervals[i+1]}.")
            
    return True