with open("fisier.txt", "r") as f:
    cuv = f.read()
s=0
cuvant = cuv.lower()
print(cuvant)
for i in cuvant:
    if ord(i) == 97 or ord(i)==105 or ord(i)==117 or ord(i)==111 or ord(i) == 101:
        s+=1
print("Numarul de vocale este", s)

