import pytest
# Remplace `character` par le nom réel de ton fichier source (ex: `from fumble.models import ...`)
from wfrp.character import Character, Characteristic, CharacteristicsCollection, SPECIES_BASE_STATS


def test_character_initialization():
    """Vérifie qu'un personnage s'initialise correctement avec ses attributs et son espèce."""
    hero = Character(
        name="Grombrindal",
        species="Nain",
        classes="Guerrier",
        career="Tueur de trolls",
        career_level="1",
        career_path="Aspirant",
        status="Bronze 1",
        age=55,
        height="1m40",
        hair="Roux",
        eyes="Bleus",
        fate=2,
        resilience=3,
        movement=3,
        experience=100
    )
    
    assert hero.name == "Grombrindal"
    assert hero.species == "Nain"
    assert hero.fate == 2
    assert hero.movement == 3
    assert hero.experience == 100
    
    # Vérifie que les stats de base du Nain ont bien été appliquées (ex: Endurence 'T' = 30 pour un nain)
    assert hero.characteristics.T.base_value == 30
    assert hero.characteristics.FEL.base_value == 10  # Le Fel des nains est à 10


def test_invalid_species_raises_error():
    """Vérifie qu'une espèce non autorisée lève bien une ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Character(
            name="Grimgor",
            species="Orque",  # Espèce interdite pour un joueur
            classes="Guerrier",
            career="Orque Noir",
            career_level="1",
            career_path="Chef",
            status="Bronze 1",
            age=30,
            height="2m10",
            hair="Chauve",
            eyes="Rouges",
            fate=1,
            resilience=2,
            movement=4,
            experience=0
        )
    
    # Optionnel mais propre : vérifier le message d'erreur
    assert "Espèce inconnu" in str(exc_info.value)

def test_characteristic_calculations():
    """Vérifie le calcul de la valeur actuelle (base + avances)."""
    stat = Characteristic("WS", base_value=30, advances=15)
    
    assert stat.base_value == 30
    assert stat.advances == 15
    assert stat.current_value == 45


@pytest.mark.parametrize("base, advances, expected_bonus", [
    (9, 0, 0),     # Frontière basse : 9 donne un bonus de 0
    (10, 0, 1),    # Frontière basse stricte : 10 donne un bonus de 1
    (35, 5, 4),    # Cas normal : 40 donne un bonus de 4
    (99, 0, 9),    # Frontière haute : 99 donne un bonus de 9
    (100, 10, 11), # Au-dessus de 100 : 110 donne un bonus de 11
])
def test_characteristic_boundaries_and_bonus(base, advances, expected_bonus):
    """Teste rigoureusement les calculs de bonus et les frontières (9/10, 99/100, etc.)."""
    stat = Characteristic("S", base_value=base, advances=advances)
    assert stat.bonus == expected_bonus