import time


def pasek_postepu(dlugosc_paska):
    for n in range(101):
        pasek = ""
        for i in range(dlugosc_paska):
            if i < int(dlugosc_paska * n / 100):
                pasek += "="
            else:
                pasek += "-"
        print(f"|{pasek}| {n}%", end='\r')
        time.sleep(0.05)



if __name__ == "__main__":
    dlugosc_paska = 50
    pasek_postepu(dlugosc_paska)
