from ZADANIE2.zadanie2 import statystyka_lancucha

def test_pusty_lancuch():
    wynik = statystyka_lancucha("")
    assert wynik["liczba_slow"] == 0
    assert wynik["liczba_liter"] == 0
    assert wynik["liczba_cyfr"] == 0
    assert wynik["statystyka"] == {}

def test_lancuch_bez_liczb_i_cyfr():
    wynik = statystyka_lancucha("Ala ma kota")
    assert wynik["liczba_slow"] == 3
    assert wynik["liczba_liter"] == 9
    assert wynik["liczba_cyfr"] == 0
    assert wynik["statystyka"] == {'a': 4, 'l': 1, 'm': 1, 'k': 1, 'o': 1, 't': 1}

def test_lancuch_z_liczbami():
    wynik = statystyka_lancucha("Ala ma 3 koty i 2 psy")
    assert wynik["liczba_slow"] == 5
    assert wynik["liczba_liter"] == 13
    assert wynik["liczba_cyfr"] == 2
    assert wynik["statystyka"] == {'a': 3, 'l': 1, 'm': 1, 'k': 1, 'o': 1, 't': 1, 'y': 2, 'i': 1, 'p': 1, 's': 1, '3': 1, '2': 1}

def test_mieszany_lancuch_ze_znakami_specjalnymi():
    wynik = statystyka_lancucha("To jest test: 123, z liczbami i literami!")
    assert wynik["liczba_slow"] == 7  
    assert wynik["liczba_liter"] == 28
    assert wynik["liczba_cyfr"] == 3
    assert wynik["statystyka"] == {
        'a': 2, 'b': 1, 'c': 1, 'e': 3, 'i': 5, 'j': 1, 'l': 2, 'm': 2, 'o': 1, 'r': 1, 's': 2, 't': 5, 'z': 2, '1': 1, '2': 1, '3': 1
    }

def test_znaki_specjalne_z_roznymi_koncami_zdan():
    wynik = statystyka_lancucha('"Ala!" "Czy to kot?" - zapytal Piotr.')
    assert wynik["liczba_slow"] == 6  # 6 słów
    assert wynik["liczba_liter"] == 23  # 23 litery
    assert wynik["liczba_cyfr"] == 0
    assert wynik["statystyka"] == {
        'a': 4, 'l': 2, 'c': 1, 'z': 2, 'y': 2, 't': 4, 'o': 3, 'k': 1, 'p': 2, 'i': 1, 'r': 1
    }

def test_zdanie_ze_znakami_i_liczbami():
    wynik = statystyka_lancucha("Czy widziales liczby: 1; 2; i 3?")
    assert wynik["liczba_slow"] == 4  # Bez liczenia cyfr jako słów
    assert wynik["liczba_liter"] == 19
    assert wynik["liczba_cyfr"] == 3
    assert wynik["statystyka"] == {
        'a': 1, 'b': 1, 'c': 2, 'd': 1, 'e': 1, 'i': 4, 'l': 2, 's': 1, 'w': 1, 'y': 2, 'z': 3, '1': 1, '2': 1, '3': 1
    }

def test_rozne_znaki_specjalne_i_spacje():
    wynik = statystyka_lancucha("!@# $$%^ &*()")
    assert wynik["liczba_slow"] == 0
    assert wynik["liczba_liter"] == 0
    assert wynik["liczba_cyfr"] == 0
    assert wynik["statystyka"] == {}
