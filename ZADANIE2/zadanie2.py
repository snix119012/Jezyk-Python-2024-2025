def cyfry(n):
    n = str(n)
    return len(n)
def rysuj_miarke(dlugosc):
    p_miarka ='0'
    miarka='|'
    for i in range(1, dlugosc+1):
        miarka+= '....|'
        p_miarka += (5 -cyfry(i)) * ' ' + f'{i}'
    miarka+= '\n' + p_miarka
    return miarka

def main():
    dlugosc_miarki = 12 # Możesz zmienić długość miarki
    miarka = rysuj_miarke(dlugosc_miarki)
    print(miarka)

if __name__ == "__main__":
    main()
