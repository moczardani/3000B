lista=[]

with open("03_000.txt" ,"r", encoding="utf8") as f:
    for szam in f:
        lista.append(int(szam))

print("9. Feladat")

print("10. Feladat")
for elem in lista:
    if elem%5==0:
        print(elem)