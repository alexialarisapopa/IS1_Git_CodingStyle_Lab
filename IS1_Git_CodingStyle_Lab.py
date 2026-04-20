import time

def calculeaza_si_afiseaza_mesaj():
    """
    Functie care afiseaza un mesaj sugestiv.
    """
    mesaj_de_afisat = "Rezultatul a fost generat cu succes."
    print(mesaj_de_afisat)

def porneste_bucla_principala():
    """
    Ruleaza functia de afisare intr-o bucla infinita la un interval de 5 secunde.
    """
    try:
        while True:
            calculeaza_si_afiseaza_mesaj()
            # Asteapta 5 secunde inainte de urmatoarea executie
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nProgram oprit de utilizator.")

if __name__ == "__main__":
    porneste_bucla_principala()
