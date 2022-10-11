zahl2 = -1

zahl1 = input("Geben sie eine Ganzahl ein")
zahl1 = int(zahl1)


while zahl2 !=0:
    zahl2 = input("Geben sie eine Ganzahl ein")
    zahl2 = int(zahl2)

    if zahl1 > 100 or zahl2 > 100:
        print ("die Zahl muss zwischen o und 100 liegen")

    elif zahl1 < zahl2:
        print("ihre zweite Zahl ist größer als die erste")

    elif zahl2 < zahl1:
        print("ihre erste Zahl ist größer als die zweite")

    elif zahl1 == zahl2:
        print("Ihre aktuelle Eingabe entspricht der letzten Eingabe")














