sciezki = []
temp = []
def zagniezdzenie(i, krok):
    global glab
    global max_glab
    global temp
    if krok == "start":
        sciezki.clear()
        temp.clear()
    temp.append(krok)
    sciezki.append(temp.copy())
    if isinstance(i,dict):
        for key , value in i.items():
            if isinstance(value,(list,dict,tuple)):
                zagniezdzenie(i.get(key), key)
        temp.pop()
        return
    if isinstance(i,(list,tuple)):
        for index, item in enumerate(i):
            if isinstance(item,(list,dict,tuple)):
                zagniezdzenie(i[index], index)
        temp.pop()
        return
    temp.pop()

def dodaj_element(wejscie):

    zagniezdzenie(wejscie,"start");
    all_paths_sorted = sorted(sciezki,key=len,reverse=True)
    print(f"all_paths_sorted{all_paths_sorted}")
    j = wejscie
    max_len = len(all_paths_sorted[0])

    added = False;
    for p in all_paths_sorted:
        current_len = len(p)
        if(max_len>current_len and added == True):
            return wejscie

        for i in range(1,len(p)):
            if isinstance(j,dict):
                j = j.get(p[i])
                continue
            j = j[p[i]]
        to_adds = [element for element in j if isinstance(element, int)]
        to_add = max(to_adds) if len(to_adds) != 0 else 0
        if(isinstance(j,tuple)):
            j = wejscie
            continue
        if(isinstance(j,list)):
            added = True
            j.append(to_add+1)
            max_len = current_len
        j = wejscie
    return wejscie

if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)

