lista = []
with open("03_000.txt", "r", encoding="utf8") as f:
    for adat in f:
        lista.append(int(adat))

def van_pozitiv(l):
    for i in l:
        if i > 0:
            return True
    return False

print(f'1. Van-e a sorozatban pozitiv szam: {"van" if van_pozitiv(lista) else "nincs"}')

print(f'2. Hany eleme van a sorozatnak: {len(lista)}')


