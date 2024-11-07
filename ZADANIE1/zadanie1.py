import sys


def rozklad_na_czynniki(n):
    wynik = []
    dzielnik = 2
    while dzielnik * dzielnik <= n:
        p = 0
        while n % dzielnik == 0:
            n //= dzielnik
            p += 1
        if p > 0:
            if p > 1:
                wynik.append(f"{dzielnik}^{p}")
            else:
                wynik.append(f"{dzielnik}")
        dzielnik += 1
    if n > 1:
        wynik.append(f"{n}")
    return "*".join(wynik)

if __name__ == "__main__":
    argv = sys.argv[1:]  # Pobieranie argumentów zewnętrznych (liczby)

    for arg in argv:
        liczba = int(arg)
        wynik = rozklad_na_czynniki(liczba)
        print(f"{liczba} = {wynik}")

