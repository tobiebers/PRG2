file1 = open("file.txt", "w")

zahl = input("geben sie eine Zahl ein")
zahl = int(zahl)
count = 0


while count != zahl:
    count = int(count)
    count = count + 1
    count = str(count)
    file1.write(count)
    count = int(count)
    print(count)

file1.close()

file1 = open("file.txt", "r")

#ganzen text einlesen
txt = file1.read()
print(txt)


