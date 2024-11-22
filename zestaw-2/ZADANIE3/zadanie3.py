def rzymskie_na_arabskie(rzymskie):
    rzymskie_w = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(rzymskie, str) or not rzymskie.isupper() or not all(c in rzymskie_w for c in rzymskie):
        raise ValueError("Niepoprawna liczba.")
    wartosc=0
    last_wartosc=0
    for i in reversed(rzymskie):
        x= rzymskie_w[i]
        if x < last_wartosc:
            wartosc-=x
        else:
            wartosc+=x
            last_wartosc=x
    if wartosc<1 or wartosc > 3999 or arabskie_na_rzymskie(wartosc)!= rzymskie:
        raise ValueError("Bledna liczba rzymska.")
    return wartosc

def arabskie_na_rzymskie(arabskie):
    rzymskie_w = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    if not isinstance(arabskie, int) or arabskie < 1 or arabskie > 3999:
        raise ValueError("Liczba musi być w zakresie 1-3999.")
    rzymskie = []
    for wartosc, symbol in rzymskie_w:
        while arabskie >= wartosc:
            rzymskie.append(symbol)
            arabskie -= wartosc

    return ''.join(rzymskie)

if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
