lista=[]

with open("03_000.txt" ,"r", encoding="utf8") as f:
    for szam in f:
        lista.append(int(szam))

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