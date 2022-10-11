file1 = open("file.txt", "w")


name = input("geben sie ihren namen ein \n")
alter = input("geben sie ihr alter ein \n")
#entweder direkt
file1.write("Hello \n")

#oder über Variablen
file1.write(name)
file1.write("\n")
file1.write(alter)

file1.close()

file1 = open("file.txt", "r")

#ganzen text einlesen
txt = file1.read()
print(txt)

file1.close()