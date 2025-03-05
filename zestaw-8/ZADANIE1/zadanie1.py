import tkinter as tk
from tkinter import messagebox
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from langdetect import detect, DetectorFactory

# Zabezpieczenie dla powtarzalności wyników langdetect
DetectorFactory.seed = 0

# Klucz API dla ElevenLabs
API_KEY = "sk_baaf6a52f0dedd0f19b897b0e587856c49cfcbe107b61c2c"

# Inicjalizacja klienta ElevenLabs
client = ElevenLabs(api_key=API_KEY)


# Funkcja do rozpoznawania języka
def detect_language():
    text = text_entry.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Uwaga", "Proszę wpisać tekst przed rozpoznaniem języka.")
        return

    try:
        lang = detect(text)
        detected_language_label.config(text=f"Rozpoznany język: {lang}")

    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się rozpoznać języka: {e}")


# Funkcja do generowania i odtwarzania dźwięku
def play_audio():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Uwaga", "Proszę wpisać tekst przed odtworzeniem audio!")
    try:
        audio = client.generate(
            text=text,
            voice="Brian",
            model="eleven_multilingual_v2"
        )
        play(audio)
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się odtworzyć: {e}")


# Tworzenie GUI
root = tk.Tk()
root.title("Generowanie audio z ElevenLabs")
root.geometry("500x350")

# Etykieta wyboru języka
language_label = tk.Label(root, text="Wpisz tekst:")
language_label.pack(pady=5)

# Pole tekstowe
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=5)

# Ramka do wyświetlania rozpoznanego języka
detected_language_frame = tk.Frame(root)
detected_language_frame.pack(pady=10)

detected_language_label = tk.Label(detected_language_frame, text="Rozpoznany język: --", fg="blue")
detected_language_label.pack()

# Przycisk do rozpoznawania języka
detect_button = tk.Button(root, text="Rozpoznaj język", command=detect_language)
detect_button.pack(pady=5)

# Przycisk odtwarzania audio
play_button = tk.Button(root, text="Odtwórz audio", command=play_audio)
play_button.pack(pady=5)

# Uruchomienie aplikacji
root.mainloop()