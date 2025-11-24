def procent_z_liczby():
    liczba = float(input("Podaj liczbę: "))
    procent = float(input("Podaj procent (1–100): "))

    wynik = liczba * (procent / 100)

    print(f"{procent}% z {liczba} = {wynik}")

procent_z_liczby()
