from ZADANIE4.zadanie4 import fun

def test_przyklad_529():
    # Liczba 529 ma binarną reprezentację 1000010001 i najdłuższą przerwę o długości 4
    assert fun(529) == 4

def test_przyklad_9():
    # Liczba 9 ma binarną reprezentację 1001 i jedną przerwę binarną o długości 2
    assert fun(9) == 2

def test_przyklad_20():
    # Liczba 20 ma binarną reprezentację 10100 i jedną przerwę binarną o długości 1
    assert fun(20) == 1

def test_brak_przerwy():
    # Liczba 15 ma binarną reprezentację 1111, więc nie ma binarnej przerwy
    assert fun(15) == 0

def test_maksymalna_przerwa():
    # Liczba 1041 ma binarną reprezentację 10000010001, gdzie najdłuższa przerwa wynosi 5
    assert fun(1041) == 5

def test_przyklad_1():
    # Liczba 1 ma binarną reprezentację 1, więc nie ma binarnej przerwy
    assert fun(1) == 0

def test_duza_liczba_2147483647():
    # Liczba 2147483647 ma binarną reprezentację 1111111111111111111111111111111, bez przerw
    assert fun(2147483647) == 0

def test_duza_liczba_z_przerwa():
    # Liczba 1342177281 ma binarną reprezentację 110000000000000000000000000001, z przerwą o długości 27
    assert fun(1342177281) == 27