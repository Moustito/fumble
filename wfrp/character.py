# --- CONFIGURATION DES ESPÈCES (Données de base WFRP 4e) ---
SPECIES_BASE_STATS = {
    "Humain": {"WS": 20, "BS": 20, "S": 20, "T": 20, "I": 20, "AG": 20, "DEX": 20, "INT": 20, "WP": 20, "FEL": 20},
    "Dwarf":   {"WS": 30, "BS": 20, "S": 20, "T": 30, "I": 20, "AG": 10, "DEX": 30, "INT": 20, "WP": 40, "FEL": 10},
    "Halfling":   {"WS": 10, "BS": 30, "S": 10, "T": 20, "I": 20, "AG": 20, "DEX": 30, "INT": 20, "WP": 30, "FEL": 30},
    "Hight elf":   {"WS": 30, "BS": 30, "S": 20, "T": 20, "I": 40, "AG": 30, "DEX": 30, "INT": 30, "WP": 30, "FEL": 20},
    "wood elf":   {"WS": 30, "BS": 30, "S": 20, "T": 20, "I": 40, "AG": 30, "DEX": 30, "INT": 30, "WP": 30, "FEL": 20},
}

# --- LA CLASSE POUR UNE SEULE CARACTÉRISTIQUE ---
class Characteristic:
    def __init__(self, name: str, base_value=0, advances=0):
        self.name = name
        self.base_value = base_value
        self.advances = advances

    @property
    def current_value(self):
        '''Calcule de la valeur current - current_value = base_values(initial) + advances'''
        return self.base_value + self.advances

    @property
    def bonus(self):
        '''Calcule du bonus de caractéristique - bonus = current_value // 10'''
        return self.current_value // 10

    def __repr__(self):
        return f"{self.name}: {self.current_value} (Bonus: {self.bonus})"

# --- LE GESTIONNAIRE DES 10 CARACTÉRISTIQUES ---
class CharacteristicsCollection:
    def __init__(self, base_values):
        self.WS = Characteristic("WS", base_values.get("WS", 20), 0)
        self.BS = Characteristic("BS", base_values.get("BS", 20), 0)
        self.S = Characteristic("S", base_values.get("S", 20), 0)
        self.T   = Characteristic("T",   base_values.get("T", 20), 0)
        self.I   = Characteristic("I",   base_values.get("I", 20), 0)
        self.AG  = Characteristic("AG",  base_values.get("AG", 20), 0)
        self.DEX = Characteristic("DEX", base_values.get("DEX", 20), 0)
        self.INT = Characteristic("INT", base_values.get("INT", 20), 0)
        self.WP  = Characteristic("WP",  base_values.get("WP", 20), 0)
        self.FEL = Characteristic("FEL", base_values.get("FEL", 20), 0)

    def __repr__(self):
        stats = [self.WS, self.BS, self.S, self.T, self.I, 
                 self.AG, self.DEX, self.INT, self.WP, self.FEL]
        return ", ".join(str(s) for s in stats)

# --- LA CLASSE PRINCIPALE : CHARACTER ---
class Character:
    VALID_SPECIES = ("Humain", "Nain", "Elfe", "Halflings")

    def __init__(
        self, 
        name, species, classes, career, career_level, career_path, 
        status, age, height, hair, eyes,
        fate, resilience, movement, experience
    ):
        # Vérification de l'espèce avant sa création.
        if not Character.is_valid_species(species):
                    raise ValueError(f"Espèce inconnu: {species!r}.")
        
        # Attributs descriptifs et d'état civil
        self.name = name
        self.species = species
        self.classes = classes
        self.career = career
        self.career_level = career_level
        self.career_path = career_path
        self.status = status
        self.age = age
        self.height = height
        self.hair = hair
        self.eyes = eyes
        
        # Attributs numériques simples
        self.fate = fate
        self.resilience = resilience
        self.movement = movement
        self.experience = experience

        # Récupération automatique des stats de base selon l'espèce
        base_stats = SPECIES_BASE_STATS.get(species, SPECIES_BASE_STATS["Humain"])
        
        # COMPOSITION : Le personnage possède son bloc de caractéristiques
        self.characteristics = CharacteristicsCollection(base_stats)

    def __repr__(self):
        return (f"Character({self.name} | Espèce: {self.species} | "
                f"Carrière: {self.career} [{self.career_level}])\n"
                f"Stats -> [{self.characteristics}]")

    @staticmethod
    def is_valid_species(species: str) -> bool:
        return species in Character.VALID_SPECIES