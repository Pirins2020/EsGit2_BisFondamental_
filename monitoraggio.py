SOGLIA_ORE = 1000

aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_volo": 1240, "controlli_ok": True},
    {"codice": "I-DEF", "modello": "B737", "ore_volo": 850, "controlli_ok": False}
]

def filtra_controlli_non_validi(lista):
    return [aero for aero in lista if not aero["controlli_ok"]]