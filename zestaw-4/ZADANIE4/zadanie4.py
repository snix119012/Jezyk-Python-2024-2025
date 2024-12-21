from multipledispatch import dispatch
import math

class Figura(object):
    def __init__(self):
        pass

class Prostokat(Figura):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    def __init__(self, x: int):
        super().__init__(x, x)

class Kolo(Figura):
    def __init__(self, r: float):
        super().__init__()
        self.r = r

# Funkcje pole
@dispatch(Figura)
def pole(instance: Figura):
    return 0

@dispatch(Prostokat)
def pole(instance: Prostokat):
    return instance.x * instance.y

@dispatch(Kwadrat)
def pole(instance: Kwadrat):
    return instance.x * instance.x

@dispatch(Kolo)
def pole(instance: Kolo):
    return math.pi * (instance.r ** 2)

@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, x: int, y: int):
    instance.x = x
    instance.y = y
    return instance.x * instance.y

@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, x: int):
    instance.x = x
    return instance.x * instance.x

@dispatch(Kolo, float)
def pole(instance: Kolo, r: float):
    instance.r = r
    return math.pi * (instance.r ** 2)

def polaPowierzchni(listaFigur):
    return [pole(i) for i in listaFigur]

if __name__ == "__main__":
    # Tworzenie obiektów
    a, b, c, d = Figura(), Prostokat(2, 4), Kwadrat(2), Kolo(3)

    # Wywołania funkcji pole
    print(f"Pole prostokąta (2x4): {pole(b)}")
    print(f"Pole kwadratu (bok=2): {pole(c)}")
    print(f"Pole koła (r=3): {pole(d)}")

    # Zmiana wymiarów za pomocą funkcji pole
    print(f"Pole prostokąta po zmianie na 5x6: {pole(b, 5, 6)}")
    print(f"Pole kwadratu po zmianie boku na 7: {pole(c, 7)}")
    print(f"Pole koła po zmianie promienia na 4: {pole(d, 4.0)}")

    # Polimorfizm
    print(polaPowierzchni([a, b, c, d]))
