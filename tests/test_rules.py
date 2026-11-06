from wfrp.rules import dice_in_array


RANGES_DATA = [
    ((1, 90), "Humain"),
    ((91, 94), "Halfling"),
    ((95, 98), "Nain"),
    (99, "Haut elfe"),
    (100, "Elfe sylvain")
]

assert dice_in_array(10, RANGES_DATA) == "Humain"
assert dice_in_array(100, RANGES_DATA) == "Elfe sylvain"
assert dice_in_array(96, RANGES_DATA) == "Nain"
print("ok")