import json
import os

from ZADANIE1.zadanie1 import process_tram_data

def test_process_tram_data():
    # Ścieżki do plików JSON, względne do lokalizacji pliku testowego
    input_file = os.path.join(os.path.dirname(__file__), '../tramwaje.json')
    
    # Oczekiwane wartości
    expected_line_stop_counts = [
        (10, 38), (50, 34), (52, 34), (9, 33), (18, 32), (14, 31), (22, 31),
        (4, 27), (13, 27), (24, 27), (1, 26), (8, 25), (11, 24), (17, 24),
        (3, 23), (19, 21), (72, 21), (5, 19), (44, 19), (49, 19),
        (20, 18), (21, 18), (16, 13)
    ]
    expected_unique_stop_count = 152

    # Wywołanie funkcji
    trams, line_stop_counts, unique_stop_count = process_tram_data(input_file)

    # Sprawdzanie zgodności wyników
    assert line_stop_counts == expected_line_stop_counts, "Nieprawidłowe line_stop_counts"
    assert unique_stop_count == expected_unique_stop_count, "Nieprawidłowa liczba unikalnych przystanków"



def test_tramwaje_out_file():
    # Oczekiwana zawartość pliku
    expected_data = {
        "1": [
            "Wańkowicza", "Cienista", "Teatr Ludowy", "Rondo Kocmyrzowskie im. Ks. Gorzelanego", "Bieńczycka", 
            "Rondo Czyżyńskie", "Centralna", "Rondo 308. Dywizjonu", "M1 al. Pokoju", "TAURON Arena Kraków al. Pokoju", 
            "Dąbie", "Ofiar Dąbia", "Fabryczna", "Francesco Nullo", "Teatr Variété", "Rondo Grzegórzeckie", 
            "Hala Targowa", "Starowiślna", "Poczta Główna", "Plac Wszystkich Świętych", "Filharmonia", 
            "UJ / AST", "Muzeum Narodowe", "Oleandry", "Park Jordana", "Reymana"
        ],
        "3": [
            "Nowy Bieżanów P+R", "Ćwiklińskiej", "Nowy Prokocim", "Teligi", "Prokocim Szpital", "Prokocim", 
            "Wlotowa", "Bieżanowska", "Kabel", "Dworcowa", "Cmentarz Podgórski", "Podgórze SKA", 
            "Plac Bohaterów Getta", "św. Wawrzyńca", "Miodowa", "Starowiślna", "Poczta Główna", 
            "Teatr Słowackiego", "Dworzec Główny Zachód", "Politechnika", "Dworzec Towarowy", 
            "Szpital Narutowicza", "Bratysławska"
        ],
        "4": [
            "Zajezdnia Nowa Huta", "Kombinat", "Struga", "Plac Centralny im. R.Reagana", "Os. Kolorowe", 
            "Rondo Czyżyńskie", "Czyżyny", "Stella-Sawickiego", "AWF", "Muzeum Lotnictwa Polskiego", 
            "TAURON Arena Kraków Wieczysta", "Białucha", "Cystersów", "Rondo Mogilskie", "Lubicz", 
            "Teatr Słowackiego", "Stary Kleparz", "Teatr Bagatela", "Batorego", "Plac Inwalidów", 
            "Urzędnicza", "Biprostal", "Uniwersytet Pedagogiczny", "Głowackiego", "Bronowice", 
            "Wesele", "Bronowice SKA"
        ],
        "5": [
            "Wańkowicza", "Cienista", "Teatr Ludowy", "Rondo Kocmyrzowskie im. Ks. Gorzelanego", "Bieńczycka", 
            "Rondo Czyżyńskie", "Czyżyny", "Stella-Sawickiego", "AWF", "Muzeum Lotnictwa Polskiego", 
            "TAURON Arena Kraków Wieczysta", "Białucha", "Cystersów", "Rondo Mogilskie", 
            "Dworzec Główny Tunel", "Politechnika", "Dworzec Towarowy", "Szpital Narutowicza", 
            "Bratysławska"
        ],
        "8": [
            "Borek Fałęcki", "Borek Fałęcki I", "Solvay", "Łagiewniki SKA", "Łagiewniki", "Rzemieślnicza", 
            "Rondo Matecznego", "Smolki", "Korona", "Plac Wolnica", "Stradom", "Wawel", "św. Gertrudy", 
            "Plac Wszystkich Świętych", "Filharmonia", "Teatr Bagatela", "Batorego", "Plac Inwalidów", 
            "Urzędnicza", "Biprostal", "Uniwersytet Pedagogiczny", "Głowackiego", "Bronowice", 
            "Wesele", "Bronowice SKA"
        ],
        "9": [
            "Mistrzejowice", "Miśnieńska", "Os. Złotego Wieku", "Rondo Piastowskie", "Dunikowskiego", 
            "Rondo Hipokratesa", "DH Wanda", "Rondo Kocmyrzowskie im. Ks. Gorzelanego", "Bieńczycka", 
            "Rondo Czyżyńskie", "Czyżyny", "Stella-Sawickiego", "AWF", "Muzeum Lotnictwa Polskiego", 
            "TAURON Arena Kraków Wieczysta", "Białucha", "Cystersów", "Rondo Mogilskie", 
            "Rondo Grzegórzeckie", "Zabłocie", "Klimeckiego", "Kuklińskiego", "Gromadzka", 
            "Lipska", "Dworzec Płaszów Estakada", "Kabel", "Bieżanowska", "Wlotowa", "Prokocim", 
            "Prokocim Szpital", "Teligi", "Nowy Prokocim", "Ćwiklińskiej"
        ],
        "10": [
            "Pleszów", "Koksochemia", "Meksyk", "Brama nr 5", "Giedroycia", "Brama nr 4", "Fort Mogiła", 
            "Bardosa", "Suche Stawy", "Klasztorna", "Os. Na Skarpie", "Plac Centralny im. R.Reagana", 
            "Os. Kolorowe", "Rondo Czyżyńskie", "Czyżyny", "Stella-Sawickiego", "AWF", 
            "Muzeum Lotnictwa Polskiego", "TAURON Arena Kraków Wieczysta", "Białucha", "Cystersów", 
            "Rondo Mogilskie", "Lubicz", "Teatr Słowackiego", "Poczta Główna", "św. Gertrudy", 
            "Wawel", "Stradom", "Plac Wolnica", "Korona", "Smolki", "Rondo Matecznego", 
            "Rzemieślnicza", "Łagiewniki", "Łagiewniki ZUS", "Łagiewniki SKA", 
            "Sanktuarium Bożego Miłosierdzia", "Turowicza"
        ],
        "11": ["Mały Płaszów P+R", "Rzebika", "Lipska", "Dworzec Płaszów Estakada", "Kabel", "Bieżanowska", 
            "Dauna", "Piaski Nowe", "Nowosądecka", "Witosa", "Kurdwanów P+R", "Kurdwanów P+R", "Turowicza", 
            "Sanktuarium Bożego Miłosierdzia", "Łagiewniki SKA", "Łagiewniki", "Brożka", "Borsucza", 
            "Lipińskiego", "Grota-Roweckiego", "Norymberska", "Ruczaj", "Kampus UJ", "Chmieleniec"
        ], 
        "13": ["Nowy Bieżanów P+R", "Ćwiklińskiej", "Nowy Prokocim", "Teligi", "Prokocim Szpital", 
            "Prokocim", "Wlotowa", "Bieżanowska", "Kabel", "Dworcowa", "Cmentarz Podgórski", "Podgórze SKA", 
            "Limanowskiego", "Korona", "Plac Wolnica", "Stradom", "Wawel", "św. Gertrudy", "Plac Wszystkich Świętych", 
            "Filharmonia", "Teatr Bagatela", "Batorego", "Plac Inwalidów", "Urzędnicza", "Biprostal", 
            "Uniwersytet Pedagogiczny", "Głowackiego"
        ], 
        "14": ["Mistrzejowice", "Miśnieńska", "Os. Złotego Wieku", "Rondo Piastowskie", "Dunikowskiego", 
            "Rondo Hipokratesa", "DH Wanda", "Rondo Kocmyrzowskie im. Ks. Gorzelanego", "Bieńczycka", 
            "Rondo Czyżyńskie", "Centralna", "Rondo 308. Dywizjonu", "M1 al. Pokoju", 
            "TAURON Arena Kraków al. Pokoju", "Dąbie", "Ofiar Dąbia", "Fabryczna", "Francesco Nullo", 
            "Teatr Variété", "Rondo Grzegórzeckie", "Rondo Mogilskie", "Lubicz", "Teatr Słowackiego", 
            "Stary Kleparz", "Teatr Bagatela", "Batorego", "Plac Inwalidów", "Urzędnicza", "Biprostal", 
            "Uniwersytet Pedagogiczny", "Głowackiego"], "16": ["Mistrzejowice", "Miśnieńska", "Os. Złotego Wieku", 
            "Rondo Piastowskie", "Dunikowskiego", "Rondo Hipokratesa", "DH Wanda", 
            "Rondo Kocmyrzowskie im. Ks. Gorzelanego", "Os. Zgody", "Plac Centralny im. R.Reagana", 
            "Os. Na Skarpie", "Klasztorna", "Suche Stawy"
        ], 
        "17": ["Czerwone Maki P+R", "Chmieleniec", "Kampus UJ", "Ruczaj", "Norymberska", "Grota-Roweckiego", 
            "Lipińskiego", "Borsucza", "Brożka", "Łagiewniki", "Łagiewniki", "Rzemieślnicza", "Rondo Matecznego", 
            "Smolki", "Korona", "Plac Bohaterów Getta", "św. Wawrzyńca", "Miodowa", "Starowiślna", "Hala Targowa", 
            "Rondo Grzegórzeckie", "Rondo Mogilskie", "Dworzec Główny Tunel", "Politechnika"\
        ], 
        "18": ["Czerwone Maki P+R", "Chmieleniec", "Kampus UJ", "Ruczaj", "Norymberska", "Grota-Roweckiego", 
            "Lipińskiego", "Kobierzyńska", "Słomiana", "Kapelanka", "Szwedzka", "Rondo Grunwaldzkie", "Orzeszkowej", 
            "Stradom", "Wawel", "św. Gertrudy", "Plac Wszystkich Świętych", "Filharmonia", "Teatr Bagatela", 
            "Stary Kleparz", "Pędzichów", "Nowy Kleparz", "Dworzec Towarowy", "Szpital Narutowicza", 
            "Bratysławska", "Krowodrza Górka P+R", "Pachońskiego P+R", "Białoprądnicka", "Górnickiego", 
            "Siewna Wiadukt", "Bociana", "Kuźnicy Kołłątajowskiej"
        ], 
        "19": ["Borek Fałęcki", "Borek Fałęcki I", "Solvay", "Łagiewniki SKA", "Łagiewniki", "Rzemieślnicza", 
            "Rondo Matecznego", "Smolki", "Korona", "Plac Bohaterów Getta", "św. Wawrzyńca", "Miodowa", 
            "Starowiślna", "Hala Targowa", "Rondo Grzegórzeckie", "Rondo Mogilskie", "Dworzec Główny Tunel", 
            "Politechnika", "Dworzec Towarowy", "Szpital Narutowicza", "Bratysławska"
        ], 
        "20": ["Mały Płaszów P+R", "Rzebika", "Lipska", "Gromadzka", "Kuklińskiego", "Klimeckiego", "Zabłocie", 
            "Rondo Grzegórzeckie", "Rondo Mogilskie", "Lubicz", "Teatr Słowackiego", "Stary Kleparz", 
            "Teatr Bagatela", "UJ / AST", "Muzeum Narodowe", "Oleandry", "Park Jordana", "Reymana"
        ], 
        "21": ["Pleszów", "Koksochemia", "Meksyk", "Brama nr 5", "Giedroycia", "Brama nr 4", "Fort Mogiła", 
            "Kopiec Wandy", "Kombinat", "Struga", "Plac Centralny im. R.Reagana", "Os. Zgody", 
            "Rondo Kocmyrzowskie im. Ks. Gorzelanego", "DH Wanda", "Rondo Hipokratesa", "Dunikowskiego", 
            "Kleeberga", "Piasta Kołodzieja"
        ], 
        "22": ["Borek Fałęcki", "Borek Fałęcki I", "Solvay", "Łagiewniki SKA", "Łagiewniki", "Brożka", \
            "Borsucza", "Kobierzyńska", "Słomiana", "Kapelanka", "Szwedzka", "Rondo Grunwaldzkie", 
            "Orzeszkowej", "Stradom", "Starowiślna", "Hala Targowa", "Rondo Grzegórzeckie", "Teatr Variété", 
            "Francesco Nullo", "Fabryczna", "Ofiar Dąbia", "Dąbie", "TAURON Arena Kraków al. Pokoju", 
            "M1 al. Pokoju", "Rondo 308. Dywizjonu", "Centralna", "Rondo Czyżyńskie", "Os. Kolorowe", 
            "Plac Centralny im. R.Reagana", "Struga", "Kombinat"
        ], 
        "24": ["Kurdwanów P+R", "Witosa", "Nowosądecka", "Piaski Nowe", "Dauna", "Bieżanowska", "Kabel", 
            "Dworcowa", "Cmentarz Podgórski", "Podgórze SKA", "Plac Bohaterów Getta", "św. Wawrzyńca", 
            "Miodowa", "Starowiślna", "Poczta Główna", "Teatr Słowackiego", "Stary Kleparz", "Teatr Bagatela", 
            "Batorego", "Plac Inwalidów", "Urzędnicza", "Biprostal", "Uniwersytet Pedagogiczny", "Głowackiego", 
            "Bronowice", "Wesele", "Bronowice SKA"
        ], 
        "44": ["Kopiec Wandy", "Kombinat", "Struga", "Plac Centralny im. R.Reagana", "Os. Kolorowe", 
            "Rondo Czyżyńskie", "Czyżyny", "Stella-Sawickiego", "AWF", "Muzeum Lotnictwa Polskiego", 
            "TAURON Arena Kraków Wieczysta", "Białucha", "Cystersów", "Rondo Mogilskie", "Lubicz", 
            "Teatr Słowackiego", "Stary Kleparz", "Pędzichów", "Nowy Kleparz"
        ], 
        "49": ["Nowy Bieżanów P+R", "Ćwiklińskiej", "Nowy Prokocim", "Teligi", "Prokocim Szpital", 
            "Prokocim", "Wlotowa", "Bieżanowska", "Kabel", "Dworzec Płaszów Estakada", "Lipska", "Gromadzka", 
            "Kuklińskiego", "Klimeckiego", "Zabłocie", "Rondo Grzegórzeckie", "Rondo Mogilskie", "Cystersów", "Białucha"
        ], 
        "50": ["Papierni Prądnickich", "Kuźnicy Kołłątajowskiej", "Bociana", "Siewna Wiadukt", "Górnickiego", 
            "Białoprądnicka", "Pachońskiego P+R", "Krowodrza Górka P+R", "Bratysławska", "Szpital Narutowicza", 
            "Dworzec Towarowy", "Politechnika", "Dworzec Główny Tunel", "Rondo Mogilskie", "Rondo Grzegórzeckie", 
            "Zabłocie", "Klimeckiego", "Kuklińskiego", "Gromadzka", "Lipska", "Dworzec Płaszów Estakada", "Kabel", 
            "Bieżanowska", "Dauna", "Piaski Nowe", "Nowosądecka", "Witosa", "Kurdwanów P+R", "Kurdwanów P+R", 
            "Turowicza", "Sanktuarium Bożego Miłosierdzia", "Łagiewniki SKA", "Solvay", "Borek Fałęcki I"
        ], 
        "52": ["Czerwone Maki P+R", "Chmieleniec", "Kampus UJ", "Ruczaj", "Norymberska", "Grota-Roweckiego", 
            "Lipińskiego", "Kobierzyńska", "Słomiana", "Kapelanka", "Szwedzka", "Rondo Grunwaldzkie", "Orzeszkowej", 
            "Stradom", "Starowiślna", "Poczta Główna", "Teatr Słowackiego", "Lubicz", "Rondo Mogilskie", "Cystersów", 
            "Białucha", "TAURON Arena Kraków Wieczysta", "Muzeum Lotnictwa Polskiego", "AWF", "Stella-Sawickiego", 
            "Czyżyny", "Rondo Czyżyńskie", "Bieńczycka", "Rondo Kocmyrzowskie im. Ks. Gorzelanego", "DH Wanda", 
            "Rondo Hipokratesa", "Dunikowskiego", "Kleeberga", "Piasta Kołodzieja"
        ],
        "72": [
            "Mały Płaszów P+R", "Rzebika", "Lipska", "Dworzec Płaszów Estakada", "Dworcowa", 
            "Cmentarz Podgórski", "Podgórze SKA", "Limanowskiego", "Korona", "Plac Wolnica", 
            "Stradom", "Wawel", "św. Gertrudy", "Plac Wszystkich Świętych", "Filharmonia", 
            "Teatr Bagatela", "Stary Kleparz", "Teatr Słowackiego", "Lubicz", 
            "Uniwersytet Ekonomiczny", "Muzeum Fotografii"
        ]
    }

    # Wywołanie funkcji
    input_file = os.path.join(os.path.dirname(__file__), '../tramwaje.json')
    trams, _, _ = process_tram_data(input_file)
    output_file = os.path.join(os.path.dirname(__file__), 'tramwaje_out.json')

    # Tymczasowe zapisanie danych do pliku wyjściowego (na potrzeby testu)
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(trams, file, ensure_ascii=False)

    # Wczytanie danych z pliku wyjściowego i sprawdzenie zgodności z oczekiwanymi danymi
    with open(output_file, 'r', encoding='utf-8') as file:
        output_data = json.load(file)

    assert output_data == expected_data, "Zawartość pliku tramwaje_out.json nie jest zgodna z oczekiwaniami"

    # Usunięcie pliku tymczasowego po teście
    os.remove(output_file)