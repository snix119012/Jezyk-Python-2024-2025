import requests
import pytest
from ZADANIE2.zadanie2 import find_crossovers, calculate_total_btc_traded

BASE_URL = 'https://zestaw2-b8fdcb958ee0.herokuapp.com/'  # Upewnij się, że to jest poprawny URL

@pytest.mark.parametrize("endpoint, local_function, is_json", [
    ("/find_crossovers", find_crossovers, True),  # Oczekujemy JSON (lista dat)
    ("/calculate_total_btc_traded", calculate_total_btc_traded, False)  # Oczekujemy liczby
])
def test_endpoint_vs_local_computation(endpoint, local_function, is_json):
    """
    Testuje, czy wyniki zwrócone przez endpointy są zgodne z lokalnymi obliczeniami funkcji.
    """
    # Pobranie wyniku z serwera.
    response = requests.get(f"{BASE_URL}{endpoint}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    if is_json:
        # Oczekujemy, że wynik będzie listą dat
        server_result = response.text.split()  # Odczytanie odpowiedzi jako tekst i rozdzielenie na listę
        local_result = local_function()  # Lokalne obliczenie, również zwraca listę dat
        assert server_result == local_result, f"Mismatch between server and local results for {endpoint}"
    else:
        # Oczekujemy, że wynik będzie liczbą całkowitą
        server_result = int(response.text)  # Odczytanie wyniku jako liczbę
        local_result = local_function()  # Lokalne obliczenie zwraca liczbę
        assert server_result == local_result, f"Mismatch between server and local results for {endpoint}"
