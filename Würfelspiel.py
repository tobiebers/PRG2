import random
zahl = random.randint(1,50)
eingabe = -1

while eingabe != zahl:
    eingabe = input("geben sie ihre Schätzung ab")
    eingabe = int(eingabe)
    zahl2 = zahl - eingabe
    zahl2 = abs(zahl2)
    print(eingabe, zahl)

    if zahl == eingabe:
        print("sie haben die richtige zahl erraten sie haben", zaehler," Versuche gebraucht")


    elif zahl2 <= 3:
        print("sie liegen shr knapp daneben")


    elif zahl2 <= 5:
        print("sie liegen knapp daneben")


    elif zahl2 <= 10:
        print("sie liegen daneben")


    else:
        print("sie liegen weit daneben")




