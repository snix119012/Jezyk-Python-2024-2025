import time
from datetime import datetime
now=datetime.now()
def wyswietl_zegar():


    while True:
        now = datetime.now()
        h = now.hour
        m = now.minute
        s = now.second
        if(s<10):
             print(f"{chr(16)}    {h}:{m}:0{s}   {chr(17)}", end='\r')
        else:
            print(f"{chr(16)}    {h}:{m}:{s}   {chr(17)}", end='\r')


if __name__ == "__main__":
    wyswietl_zegar()
