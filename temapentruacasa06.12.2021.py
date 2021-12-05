lista1 = []
note=[]
with open("lista.txt", "r")as f:
    lista = f.readlines()
    for i in lista:
        lista1.append(i[0:-1])
print("Nume", "Prenume", "Nota", "Obiectul")
for i in lista1:
    print(i)
    for x in i.split():
        if x.isdigit():
            note.append(int(x))
print("Nota medie a clasei este: ", sum(note)/len(note))

with open("Germana.txt", "w") as g:
    z=[]
    s=0
    g.write("Nume "+ "Prenume "+ "Nota "+  "Obiectul" + "\n")
    for i in lista1:
        if i[-3:-1]=="an":
            g.write(str(i)+"\n")
            for x in i.split():
                if x.isdigit():
                    z.append(int(x))
    g.write("Nota medie a clasei la Germana este: "+ str(round(sum(z)/len(z), 2)))
with open("Engleza.txt", "w") as e:
    m=[]
    s=0
    e.write("Nume "+ "Prenume "+ "Nota "+  "Obiectul"+"\n")
    for i in lista1:
        if i[-3:-1]=="ez":
            e.write(str(i)+"\n")
            for x in i.split():
                if x.isdigit():
                    m.append(int(x))
    e.write("Nota medie a clasei la Engleza este: " + str(round(sum(m)/len(m), 2)))
                                    


