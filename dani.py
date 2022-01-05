lista = []
with open("03_000.txt", "r", encoding="utf8") as f:
    for adat in f:
        lista.append(int(adat))

def van_pozitiv(l):
    for i in l:
        if i > 0:
            return True
    return False

def legkisebb(l):
    min = l[0]
    for i in l:
        if i<min:
            min = i
    return min

def harmincharom(l):
    index = 0
    for i in l:
        if i%33 == 0:
            return index
        index += 1

def atlagfele(l):
    osszeg = 0
    for i in l:
        osszeg+=i
    return (osszeg/len(l))/2

def minden_szam_pozitiv(l):
    for i in l:
        if i <= 0:
            return False
    return True

print(f'1. Van-e a sorozatban pozitiv szam: {"van" if van_pozitiv(lista) else "nincs"}')

print(f'2. Hany eleme van a sorozatnak: {len(lista)}')

print(f'3. Mennyi a sorozatban található legkisebb szám?: {legkisebb(lista)}')

print(f'4. Írjuk ki az első 33-mal osztható szám indexét!: {harmincharom(lista)}')

print(f'5. Mennyi a sorozatban található számok átlagának a fele?: {atlagfele(lista)}')

print(f'6. Igaz-e, hogy minden szám pozitív? {"Igaz" if minden_szam_pozitiv(lista) else "Hamis"}')