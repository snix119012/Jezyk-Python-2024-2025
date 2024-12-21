import json
import re



def process_tram_data(input_file):
    output_file='tramwaje_out.json'
    with open(input_file, "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
    trams = {}
    stop_counts = {}
    all_stops = set()

    for tram in data['tramwaje']:
        line_number = int(tram['linia'])
        stops = tram['przystanek']

        stop_names = tuple(re.sub(r'\s\d+$', '', stop['nazwa']) for stop in stops)
        trams[line_number] = stop_names
        stop_counts[line_number] = len(stop_names)
        all_stops.update(stop_names)

    line_stop_counts = sorted(stop_counts.items(), key=lambda x: x[1], reverse=True)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(trams, file, ensure_ascii=False)

    return trams, line_stop_counts, len(all_stops)

if __name__ == '__main__':
    trams, line_stop_counts, unique_stop_count = process_tram_data('tramwaje.json')

    print("Linia - liczba przystanków (posortowane malejąco):")
    for line, count in line_stop_counts:
        print(f"Linia {line}: {count} przystanków")

    print(f"Liczba wszystkich unikalnych przystanków: {unique_stop_count}")
    line_number = 52
    if line_number in trams:
        print(f"\nPrzystanki dla linii {line_number}:")
        for stop in trams[line_number]:
            print(stop)
