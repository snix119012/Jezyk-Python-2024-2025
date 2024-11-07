from ZADANIE2.zadanie2 import rysuj_miarke

# Poprawiony test skrajnego przypadku - długość 0
def test_miarka_0():
    oczekiwany_wynik = "|\n0"
    assert rysuj_miarke(0) == oczekiwany_wynik

# Test dla długości 1
def test_miarka_1():
    oczekiwany_wynik = "|....|\n0    1"
    assert rysuj_miarke(1) == oczekiwany_wynik

# Test dla długości 2
def test_miarka_2():
    oczekiwany_wynik = "|....|....|\n0    1    2"
    assert rysuj_miarke(2) == oczekiwany_wynik

# Test dla długości 10
def test_miarka_10():
    oczekiwany_wynik = (
        "|....|....|....|....|....|....|....|....|....|....|\n"
        "0    1    2    3    4    5    6    7    8    9   10"
    )
    assert rysuj_miarke(10) == oczekiwany_wynik

# Test dla długości 12
def test_miarka_12():
    oczekiwany_wynik = (
        "|....|....|....|....|....|....|....|....|....|....|....|....|\n"
        "0    1    2    3    4    5    6    7    8    9   10   11   12"
    )
    assert rysuj_miarke(12) == oczekiwany_wynik

# Test dla ekstremalnego przypadku 999 (sprawdzamy tylko pierwsze 50 znaków i ostatnie 50)
def test_miarka_999():
    wynik = rysuj_miarke(999)
    # Sprawdź pierwsze 50 znaków
    assert wynik.startswith("|....|....|....|....|....|....|....|....|....|....|")
    # Sprawdź ostatnie 50 znaków
    assert wynik.endswith("  997  998  999")

# Test dla liczby wielocyfrowej - długość 123
def test_miarka_123():
    oczekiwany_wynik = (
        "|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|\n"
        "0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58   59   60   61   62   63   64   65   66   67   68   69   70   71   72   73   74   75   76   77   78   79   80   81   82   83   84   85   86   87   88   89   90   91   92   93   94   95   96   97   98   99  100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118  119  120  121  122  123"
    )
    assert rysuj_miarke(123) == oczekiwany_wynik
