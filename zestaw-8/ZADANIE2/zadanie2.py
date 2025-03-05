import tkinter as tk
import cv2
from PIL import Image, ImageTk
import threading
import time

# Główne okno aplikacji
window = tk.Tk()
window.title("Streaming z kamerki - kontrola filtrów")
window.geometry("340x300")  # Dopasowany rozmiar okna

# Zmienna globalna do zarządzania streamingiem i filtrem
streaming = False
filter_mode = None

# Funkcja do uruchamiania/wyłączania streamingu
def toggle_streaming():
    global streaming
    streaming = not streaming
    if streaming:
        start_button.config(text="Stop")
        threading.Thread(target=stream_camera).start()
    else:
        start_button.config(text="Start")

# Funkcja do ustawiania trybu filtru
def set_filter(mode):
    global filter_mode
    filter_mode = mode

# Funkcja do obsługi kamery i wyświetlania wideo
def stream_camera():
        # twój kod
        # zakładam, że ramka będzie mieć nazwę frame

        # Konwersja do formatu akceptowanego przez tkinter
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        # Wyświetlanie wideo w tkinter
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

        # Czekaj, aby osiągnąć niższą liczbę klatek na sekundę
        time.sleep(0.1)  # Ograniczenie do około 10 klatek na sekundę

    # koniec streamingu



# Widgety tkinter
# Panel sterowania - przyciski u góry okna
control_panel = tk.Frame(window)
control_panel.pack(side=tk.TOP, pady=5)

# Przycisk Start/Stop
start_button = tk.Button(control_panel, text="Start", command=toggle_streaming)
start_button.pack(side=tk.LEFT, padx=5)

# Przycisk wyboru filtru czerwonego
red_button = tk.Button(control_panel, text="Czerwony", command=lambda: set_filter("R"))
red_button.pack(side=tk.LEFT, padx=5)

# Przycisk wyboru filtru zielonego
green_button = tk.Button(control_panel, text="Zielony", command=lambda: set_filter("G"))
green_button.pack(side=tk.LEFT, padx=5)

# Przycisk wyboru filtru niebieskiego
blue_button = tk.Button(control_panel, text="Niebieski", command=lambda: set_filter("B"))
blue_button.pack(side=tk.LEFT, padx=5)

# Przycisk wyboru filtru czarno-białego
gray_button = tk.Button(control_panel, text="Czarno-biały", command=lambda: set_filter("gray"))
gray_button.pack(side=tk.LEFT, padx=5)

# Przycisk przywracający pełny kolor
reset_button = tk.Button(control_panel, text="Kolor", command=lambda: set_filter(None))
reset_button.pack(side=tk.LEFT, padx=5)

# Etykieta wideo poniżej przycisków
video_label = tk.Label(window)
video_label.pack(side=tk.TOP, padx=10, pady=10)

# Uruchomienie okna
window.mainloop()