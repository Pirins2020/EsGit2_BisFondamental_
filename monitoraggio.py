SOGLIA_ORE = 1000

aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_volo": 670, "controlli": True},
    {"codice": "I-DEF", "modello": "Boeing 737", "ore_volo": 700, "controlli": False},
    {"codice": "I-GHI", "modello": "Boeing 737", "ore_volo": 370, "controlli": False},
    {"codice": "I-JKL", "modello": "Airbus", "ore_volo": 450, "controlli": True}
]

def stampa_riepilogo(lista):
    print("=== RIEPILOGO FLOTTA ===")
    for aero in lista:
        stato = "OK" if aero["controlli_ok"] else "INSPECTION NEEDED"
        print(f"[{aero['codice']}] Modello: {aero['modello']} | Ore: {aero['ore_volo']} | Controlli: {stato}")