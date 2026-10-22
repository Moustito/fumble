import pytest
import random

from wfrp.dice import dice_throw


# 1. Vérification que le résultat est toujours compris entre 1 et n (sur un grand nombre de jets)
@pytest.mark.parametrize("n_faces", [2, 6, 20, 100])
def test_dice_throw_range(n_faces):
    for _ in range(1000):
        result = dice_throw(n_faces)
        assert 1 <= result <= n_faces


# 2. Vérification qu'avec la même graine, on obtient la même suite de résultats
def test_dice_throw_reproducibility():
    seed_value = 42
    
    # Premier tirage avec la graine
    random.seed(seed_value)
    sequence_1 = [dice_throw(6) for _ in range(10)]
    
    # Deuxième tirage avec la même graine
    random.seed(seed_value)
    sequence_2 = [dice_throw(6) for _ in range(10)]
    
    assert sequence_1 == sequence_2


# 3. Vérification qu'un nombre de faces invalide lève une ValueError
@pytest.mark.parametrize("invalid_n", [0, -1, -10])
def test_dice_throw_invalid_faces(invalid_n):
    # Note : random.randrange lève de base une ValueError si l'intervalle est invalide (stop <= start).
    # Si ta fonction gère cela explicitement ou via random, le test passera.
    with pytest.raises(ValueError):
        dice_throw(invalid_n)

# 3. Vérification qu'un mauvais type de paramètre lève une ValueError
@pytest.mark.parametrize("invalid_type_input", [6.5, "6", "six", True, None])
def test_dice_invalid_types(invalid_type_input):
    with pytest.raises(ValueError):
        dice_throw(invalid_type_input)