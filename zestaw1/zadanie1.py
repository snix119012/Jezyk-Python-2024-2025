import sys

def rozklad_na_czynniki(x):
    i = 2
    czynniki = []
    while x > 1:
        ilosc = 0
        while x % i == 0:
            ilosc += 1
            x //= i
        if ilosc > 0:
            czynniki.append((i, ilosc))
        i += 1
    return czynniki

def formatuj_wynik(czynniki):
    wynik = []
    for liczba_pierwsza, i in czynniki:
        if i == 1:
            wynik.append(f"{liczba_pierwsza}")
        else:
            wynik.append(f"{liczba_pierwsza}^{i}")
    return "*".join(wynik)

if __name__ == "__main__":
    args = sys.argv[1:]

    for arg in args:
        liczba = int(arg)
        czynniki = rozklad_na_czynniki(liczba)
        sformatowane = formatuj_wynik(czynniki)
        print(f"{liczba} = {sformatowane}")
