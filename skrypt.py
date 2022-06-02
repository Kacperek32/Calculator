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