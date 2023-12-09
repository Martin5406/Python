import random
import json

f = open('data.json')
data = json.load(f)

for i in data['emp_details']:
	print(i)
f.close()

def hra():
    print("Vítejte ve hře Chcete být milionářem!")
    jmeno = input("Jaké je tvé jméno?:")
    print("Vítej", jmeno + "!")

    otazky = 0
    vyhra = 0

    while otazky < 1:
        print("\nZačněme otázkou č.", otazky + 1, "Za 10000$")
        otazka, moznosti, odpoved = get_otazky()
        print(otazka)
        for key, value in moznosti.items():
            print(key + ") " + value)
        user_odpoved = input("Zadejte písmeno správné odpovědi:")
        if user_odpoved.lower() == odpoved.lower():
            print("Správně!")
            vyhra += 10000
            otazky += 1
        else:
            print("Špatně!")
            print("Gratulujeme! Vyhráli jste", vyhra, "$")
            break
    
    if otazky > 0:
        while vyhra < 100000:
            print("\nPokračujme otázkou č.", otazky + 1, "Za", vyhra+10000,"$!")
            otazka, moznosti, odpoved = get_otazky()
            print(otazka)
            for key, value in moznosti.items():
                print(key + ") " + value)
            user_odpoved = input("Zadejte písmeno správné odpovědi:")
            if user_odpoved.lower() == odpoved.lower():
                print("Správně!")
                vyhra += 10000
                otazky += 1
            else:
                print("Špatně!")
                break
        
        if vyhra == 100000:
            print("Gratuluji! Vyhrál jste nejvyšší možnou výhru 100 000 $!")

hra()
