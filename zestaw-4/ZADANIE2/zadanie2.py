from abc import ABC, abstractmethod

class Pojazd(ABC):
    def __init__(self, model: str, rok: int):
        self._model = model
        self._rok = rok
        self._predkosc = 0

    @property
    def predkosc(self) -> float:
        return self._predkosc

    @predkosc.setter
    def predkosc(self, value: float):
        if value < 0:
            raise ValueError("Prędkość nie może być ujemna!")
        self._predkosc = value

    @predkosc.deleter
    def predkosc(self):
        self._predkosc = 0


class Samochod(Pojazd):
    def __init__(self, model: str, rok: int, liczba_drzwi: int):
        super().__init__(model, rok)
        self.liczba_drzwi = liczba_drzwi


class Autobus(Pojazd):
    def __init__(self, model: str, rok: int, liczba_miejsc: int):
        super().__init__(model, rok)
        self.liczba_miejsc = liczba_miejsc


class FabrykaPojazdow(ABC):
    def __init__(self, nazwa: str):
        self._nazwa = nazwa
        self._liczba_wyprodukowanych = 0

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @staticmethod
    def sprawdz_rok(rok: int) -> bool:
        return 1900 <= rok <= 2024

    @classmethod
    def utworz_fabryke(cls, typ_fabryki: str, nazwa: str):
        if typ_fabryki == 'samochod':
            return FabrykaSamochodow(nazwa)
        elif typ_fabryki == 'autobus':
            return FabrykaAutobusow(nazwa)
        else:
            raise ValueError("Nieznany typ fabryki")

    def _zwieksz_licznik(self):
        self._liczba_wyprodukowanych += 1

    def ile_wyprodukowano(self) -> int:
        return self._liczba_wyprodukowanych

    @abstractmethod
    def stworz_pojazd(self, model: str, rok: int, **kwargs) -> Pojazd:
        if not self.sprawdz_rok(rok):
            raise ValueError("Nieprawidłowy rok produkcji!")

class FabrykaSamochodow(FabrykaPojazdow):
    def stworz_pojazd(self, model: str, rok: int, liczba_drzwi: int = 4) -> Samochod:
        if not self.sprawdz_rok(rok):
            raise ValueError("Nieprawidłowy rok produkcji!")
        pojazd = Samochod(model, rok, liczba_drzwi)
        self._zwieksz_licznik()
        return pojazd


class FabrykaAutobusow(FabrykaPojazdow):
    def stworz_pojazd(self, model: str, rok: int, liczba_miejsc: int = 50) -> Autobus:
        if not self.sprawdz_rok(rok):
            raise ValueError("Nieprawidłowy rok produkcji!")
        pojazd = Autobus(model, rok, liczba_miejsc)
        self._zwieksz_licznik()
        return pojazd


def main():
    # Utwórz fabryki pojazdów (samochodów i autobusów)
    fabryka_samochodow = FabrykaPojazdow.utworz_fabryke('samochod', "Fabryka Samochodów Warszawa")
    fabryka_autobusow = FabrykaPojazdow.utworz_fabryke('autobus', "Fabryka Autobusów Kraków")

    # Utworzone fabryki - demonstracja @property nazwa
    print(f"Nazwa fabryki: {fabryka_samochodow.nazwa}")
    print(f"Nazwa fabryki: {fabryka_autobusow.nazwa}")

    # Utwórz pojazdy
    samochod = fabryka_samochodow.stworz_pojazd("Fiat", 2023, liczba_drzwi=5)
    autobus = fabryka_autobusow.stworz_pojazd("Solaris", 2023, liczba_miejsc=60)

    # Demonstracja działania gettera, settera i deletera
    samochod.predkosc = 50  # użycie settera
    print(f"Prędkość samochodu: {samochod.predkosc}")  # użycie gettera
    del samochod.predkosc  # użycie deletera
    print(f"Prędkość po resecie: {samochod.predkosc}")

    # Pokazanie ile pojazdów wyprodukowano
    print(f"Wyprodukowano samochodów: {fabryka_samochodow.ile_wyprodukowano()}")
    print(f"Wyprodukowano autobusów: {fabryka_autobusow.ile_wyprodukowano()}")


if __name__ == "__main__":
    main()
