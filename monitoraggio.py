SOGLIA_ORE = 1000

aeromobili = [
    {"codice": "I-ABC", "modello": "Boeing 747", "ore_volo": 1240, "controlli_ok": True},
    {"codice": "I-DEF", "modello": "F-16", "ore_volo": 850, "controlli_ok": False},
    {"codice": "I-GHI", "modello": "Messerschmitt Me262", "ore_volo": 1500, "controlli_ok": False},
    {"codice": "I-JKL", "modello": "Mustang p-51", "ore_volo": 450, "controlli_ok": True}
]

def stampa_riepilogo(lista):
    print("=== RIEPILOGO FLOTTA ===")
    if not lista:
        print("Nessun aeromobile presente in flotta.")
        return
    for aero in lista:
        stato = "OK" if aero["controlli_ok"] else "INSPECTION NEEDED"
        print(f"[{aero['codice']}] Modello: {aero['modello']} | Ore: {aero['ore_volo']} | Controlli: {stato}")

def filtra_controlli_non_validi(lista):
    return [aero for aero in lista if not aero["controlli_ok"]]

def filtra_oltre_soglia(lista, soglia):
    return [aero for aero in lista if aero["ore_volo"] > soglia]

def stampa_segnalazioni(titolo, lista, info_key):
    print(f"\n=== {titolo} ===")
    if not lista:
        print("Nessuna segnalazione presente.")
    else:
        for aero in lista:
            print(f"[{aero['codice']}] Modello: {aero['modello']} - {info_key}: {aero[info_key]}")

if __name__ == "__main__":
    stampa_riepilogo(aeromobili)
    
    non_validi = filtra_controlli_non_validi(aeromobili)
    stampa_segnalazioni("SEGNALAZIONI: CONTROLLI NON VALIDI", non_validi, "controlli_ok")
    
    oltre_soglia = filtra_oltre_soglia(aeromobili, SOGLIA_ORE)
    stampa_segnalazioni(f"SEGNALAZIONI: OLTRE SOGLIA ({SOGLIA_ORE} ORE)", oltre_soglia, "ore_volo")