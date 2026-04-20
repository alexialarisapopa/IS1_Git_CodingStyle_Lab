import time

def genereaza_sir_fibonacci(numar_termeni):
    """
    Calculeaza si returneaza o lista cu primele n numere din sirul Fibonacci.
    """
    termen_anterior = 0
    termen_curent = 1
    sir_rezultat = []

    for _ in range(numar_termeni):
        sir_rezultat.append(termen_anterior)
        # Calculam urmatorul termen prin suma ultimelor doua
        urmatorul_termen = termen_anterior + termen_curent
        termen_anterior = termen_curent
        termen_curent = urmatorul_termen
        
    return sir_rezultat

def ruleaza_programul():
    """
    Executa generarea sirului la fiecare 5 secunde.
    """
    numar_elemente = 10
    
    try:
        while True:
            rezultat = genereaza_sir_fibonacci(numar_elemente)
            print(f"Sirul Fibonacci ({numar_elemente} termeni): {rezultat}")
            
            # Asteptam 5 secunde inainte de regenerare
            print("Se asteapta 5 secunde pentru regenerare...\n")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nProgram oprit de utilizator.")

if __name__ == "__main__":
    ruleaza_programul()
