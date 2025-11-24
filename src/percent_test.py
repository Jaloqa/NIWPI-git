def procent_z_liczby():
    liczba = float(input("Podaj liczbę: "))
    procent = float(input("Podaj procent (1–100): "))

    wynik = liczba * (procent / 100)

    print(f"{procent}% z {liczba} = {wynik}")

procent_z_liczby()
if __name__ == "__main__":
    procent_z_liczby()
    
    
    
def podwyzka_procentowa():
    liczba = float(input("Podaj liczbę: "))
    procent = float(input("Podaj procent podwyżki: "))

    wynik = liczba * (1 + procent / 100)

    print(f"Po podwyżce o {procent}%: {wynik}")
