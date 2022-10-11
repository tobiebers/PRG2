inp = -1
sum = 0
while inp != 0:
    if inp >= 10:
        print("Diese Eingabe wird übersprungen.")
    else:
        inp = input("Bitte geben Sie eine Zahl ein: ")
        inp = int(inp)
        sum = sum + inp
        print("Summe: ", sum)