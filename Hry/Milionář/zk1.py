import random
import json

with open("otázky.JSON", encoding="utf-8") as f:
    data = json.load(f)

def nacteni_otazek(vybrane_otazky):
    dostupne_otazky = []

    for i in range(len(data["otazky"])):
        if i not in vybrane_otazky:
            dostupne_otazky.append(i)

    otazka_index = random.choice(dostupne_otazky)

    return data["otazky"][otazka_index], otazka_index

def hra():
    print("Vítejte ve hře Chcete být milionářem!")
    jmeno = input("Jaké je tvé jméno?:")
    print("Vítej", jmeno + "!")

    otazky = 0
    vyhra = 0
    vybrane_otazky = []

    while otazky < 1:
        print("\nZačněme otázkou č.", otazky + 1, "za 10 000 $")

        otazka, otazka_index = nacteni_otazek(vybrane_otazky)

        print(otazka["otazka"])
        for moznost, odpoved in otazka["moznosti"].items():
            print(moznost + ") " + odpoved)

        user_odpoved = input("Zadejte písmeno správné odpovědi:")

        if user_odpoved.lower() == otazka["odpoved"].lower():
            print("Správně!")
            vyhra += 10000
            otazky += 1
            vybrane_otazky.append(otazka_index)
        else:
            print("Špatně!")
            print("Správná odpověď je:", otazka["odpoved"])
            print("Bohužel dnes se nezadařilo. Vaše výhra činí:", vyhra, "$")
            break

    if otazky > 0:
        while vyhra < 90000:
            print("\nPokračujme otázkou č.", otazky + 1, "za", vyhra+10000,"$!")

            otazka, otazka_index = nacteni_otazek(vybrane_otazky)

            print(otazka["otazka"])
            for moznost, odpoved in otazka["moznosti"].items():
                print(moznost + ") " + odpoved)

            user_odpoved = input("Zadejte písmeno správné odpovědi:")

            if user_odpoved.lower() == otazka["odpoved"].lower():
                print("Správně!")
                vyhra += 10000
                otazky += 1
                vybrane_otazky.append(otazka_index)
            else:
                print("Špatně!")
                print("Správná odpověď je:", otazka["odpoved"])
                print("Gratulujeme! Vaše výhra činí:", vyhra, "$!")
                break

    if vyhra >= 90000 and otazky == 9:
        print("\nA poslední otázka za nejvyšší možnou výhru! Otázkou č.", otazky + 1, "za", vyhra+10000,"$!")

        otazka, otazka_index = nacteni_otazek(vybrane_otazky)

        print(otazka["otazka"])
        for moznost, odpoved in otazka["moznosti"].items():
            print(moznost + ") " + odpoved)

        user_odpoved = input("Zadejte písmeno správné odpovědi:")

        if user_odpoved.lower() == otazka["odpoved"].lower():
            print("Správně!")
            vyhra += 10000
            otazky += 1
            vybrane_otazky.append(otazka_index)
        else:
            print("Špatně!")
            print("Správná odpověď je:", otazka["odpoved"])
            print("Gratulujeme! Vaše výhra činí:", vyhra, "$!")
    if vyhra == 100000:
        print("Gratuluji! Vyhrál jste nejvyšší možnou výhru 100 000 $!")

hra()
