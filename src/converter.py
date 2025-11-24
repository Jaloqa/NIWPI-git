def wizualizacja_c_to_f(c):
    f = c_to_f(c)

    print("\n   [ Konwersja ]")
    print(f"   {c}°C  ─────▶  {f}°F")
    print("        🔥")



def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9


def konwerter_temperatur():
    print("=== Konwerter temperatur ===")
    print("1. Celsjusz → Fahrenheit")
    print("2. Fahrenheit → Celsjusz")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        c = float(input("Podaj °C: "))
        f = c_to_f(c)
        print(f"{c}°C = {f}°F")

    elif wybor == "2":
        f = float(input("Podaj °F: "))
        c = f_to_c(f)
        print(f"{f}°F = {c}°C")

    else:
        print("Niepoprawny wybór.")
