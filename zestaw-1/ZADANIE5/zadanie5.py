import os
import time


def wyczysc_ekran():
    # Czyszczenie ekranu w zależności od systemu operacyjnego
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux/Mac


def przesun_tekst_w_pionie(tekst, wysokosc_okna, opoznienie=0.1):
    while True:
        for i in range(0, wysokosc_okna):
            print("\n" * i)
            print(tekst)
            time.sleep(opoznienie)
            wyczysc_ekran()
        for i in range(wysokosc_okna-2, -1, -1):
            print("\n" * i)
            print(tekst)
            time.sleep(opoznienie)
            wyczysc_ekran()


if __name__ == "__main__":
    tekst = "  Hello world!  "  # Tekst do przesuwania
    wysokosc_okna = 10  # Wysokość "okna" terminala
    przesun_tekst_w_pionie(tekst, wysokosc_okna)
