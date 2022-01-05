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

print(f'1. Van-e a sorozatban pozitiv szam: {"van" if van_pozitiv(lista) else "nincs"}')

print(f'2. Hany eleme van a sorozatnak: {len(lista)}')

print(f'3. Mennyi a sorozatban található legkisebb szám?: {legkisebb(lista)}')

print(f'4. Írjuk ki az első 33-mal osztható szám indexét!: {harmincharom(lista)}')

print(f'5. Mennyi a sorozatban található számok átlagának a fele?: {atlagfele(lista)}')

print("6. Feladat")
igaze=1
for elem in lista:
    if elem <1:
        igaze=0
        break
if igaze==1:
    print("Igaz")
else:
    print("Nem")

print("7. Feladat")
db=0
for elem in lista:
    if elem%2==1:
        db+=1
print(db)

print("8. Feladat")
elozo="poz"
for elem in lista:
    if elem<0 and elozo=="neg":
        print("Van")
        break
    if elem<0:
        elozo="neg"
    else:
        elozo="poz"

print("9. Feladat")
index=0
oszthato=-1
for elem in lista:
    if elem%19==0:
        oszthato=index
    index+=1
print(oszthato)

print("10. Feladat")
for elem in lista:
    if elem%5==0:
        print(elem)