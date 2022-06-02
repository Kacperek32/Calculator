import logging
logging.basicConfig(level=logging.DEBUG)

def sub(number, number3):
    return number - number3
def add(number, number3):
    return number + number3
def multi(number, number3):
    return number * number3
def div(number, number3):
    return number / number3

calculating = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
if calculating in ("1", "2", "3", "4"):
    number1 = float(input("Podaj składnik 1: "))
    number2 = float(input("Podaj składnik 2: "))

    if calculating == "1":
        wynik = f"Wynik to {add(number1, number2)}"
        print(wynik)
        logging.info("Dodaję teraz")
    elif calculating == "2":
        wynik2 = f"Wynik to {sub(number1, number2)}"
        print(wynik2)
        logging.info("Odejmuję teraz")
    elif calculating == "3":
        logging.info("Mnozę teraz")
        wynik3 = f"Wynik to {multi(number1, number2)}"
        print(wynik3)
    elif calculating == "4":
        logging.info("Dzielę teraz")
        wynik4 = f"Wynik to {div(number1, number2)}"
        print(wynik4)