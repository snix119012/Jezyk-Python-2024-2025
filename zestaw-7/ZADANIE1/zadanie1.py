import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar
import os

os.environ['TK_SILENCE_DEPRECATION'] = '1'
okno = tk.Tk()
okno.title("Zegar i kalendarz")
okno.geometry("400x600")
okno.resizable(False, False)

# utwórz StringVar()
date_time_var = StringVar()

def update_date_time():
    dzien = datetime.today().strftime('%A')
    miesiac = datetime.today().strftime('%B')
    rok = datetime.today().strftime('%Y')
    czas = datetime.today().strftime('%H:%M:%S')
    data = datetime.today().strftime('%d.%m.%Y')
    dt = f"{dzien}\n{data}\n{czas}"
    date_time_var.set(dt)

    date_time.after(1000, update_date_time)


date_time = Label(
    okno,
    textvariable=date_time_var,
    font=('Arial', 24),
    bg='lightpink',
    width=40,
    height=5
)
date_time.pack(anchor="center", pady=20)

current_time = datetime.now()
day = int(current_time.strftime('%d'))
month = int(current_time.strftime('%m'))
year = int(current_time.strftime('%Y'))

cal = Calendar(
    okno,
    selectmode='day',
    year=year,
    month=month,
    day=day,
    font=('Arial', 14),
    background='white',
    foreground='black',
    selectbackground='lightpink',
    selectforeground='white'
)
cal.pack(pady=20)

update_date_time()
okno.mainloop()