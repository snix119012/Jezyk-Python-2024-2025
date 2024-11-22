from collections import Counter
def statystyka_lancucha(tekst):
    tekst = tekst.lower()
    liczba_slow = 0
    liczba_liter = sum(1 for c in tekst if c.isalpha())
    liczba_cyfr = sum(1 for c in tekst if c.isdigit())
    fragmenty = tekst.split()
    for fragment in fragmenty:
        if any(c.isalpha() for c in fragment):
            liczba_slow += 1
    licznik = Counter(c for c in tekst if c.isalnum())
    statystyka_posortowana = {k: licznik[k] for k in sorted(licznik) if licznik[k] > 0}
    return {
        "liczba_slow": liczba_slow,
        "liczba_liter": liczba_liter,
        "liczba_cyfr": liczba_cyfr,
        "statystyka": statystyka_posortowana
    }

if __name__ == "__main__":
    tekst_wejsciowy = "Ala ma 3 koty i 2 psy"
    wynik = statystyka_lancucha(tekst_wejsciowy)

    print("Liczba słów:", wynik["liczba_slow"])
    print("Liczba liter:", wynik["liczba_liter"])
    print("Liczba cyfr:", wynik["liczba_cyfr"])
    print("Statystyka częstości występowania:")
    for znak, liczba in wynik["statystyka"].items():
        print(f"'{znak}': {liczba}", end=" ")
