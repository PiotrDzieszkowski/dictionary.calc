import logging
logging.basicConfig(level=logging.DEBUG)

def calculate(x, y, operation):
    operations ={"1": lambda a, b: x + y, "2": lambda a, b: x - y, "3": lambda a, b: x * y, "4": lambda a, b: x / y, "5": lambda a, b: x % y}
    return operations[operation](x, y)

def main():
    print("Kalkulator")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Procent")
    koniec = False
    while not koniec:
       a = int(input("Podaj pierwszą liczbę: "))
       b = int(input("Podaj drugą liczbę: "))
       działanie = input("Wybierz działanie: ")
       print(calculate(a, b, działanie))
     
    
if __name__ == "__main__":
    main()