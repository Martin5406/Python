import random
import json

with open("otázky.JSON", encoding="utf-8") as f:
    data = json.load(f)

def nacteni_otazek(vybrane_otazky):
    

def hra():
    print("Vítejte ve hře Chcete být milionářem!")
    jmeno = input("Jaké je tvé jméno?:")
    print("Vítej", jmeno + "!")

    otazky = 0
    vyhra = 0
    vybrane_otazky = []

    while otazky < 1:
        print("\nZačněme otázkou č.", otazky + 1, "Za 10000$")
        otazka, otazka_index = nacteni_otazek(vybrane_otazky)
        
        print(otazka["otazka"])
        for key, value in otazka["moznosti"].items():
            print(key + ") " + value)
        
        user_odpoved = input("Zadejte písmeno správné odpovědi:")
        
        if user_odpoved.lower() == otazka["odpoved"].lower():
            print("Správně!")
            vyhra += 10000
            otazky += 1
            vybrane_otazky.append(otazka_index)
        else:
            print("Špatně!")
            print("Gratulujeme! Vyhráli jste", vyhra, "$")
            break
    
    if otazky > 0:
        while vyhra < 100000:
            print("\nPokračujme otázkou č.", otazky + 1, "Za", vyhra+10000,"$!")
            otazka, otazka_index = nacteni_otazek(vybrane_otazky)
            
            if otazka is None:
                print("Nemáme dostatek otázek k dispozici.")
                break
            
            print(otazka["otazka"])
            for key, value in otazka["moznosti"].items():
                print(key + ") " + value)
            
            user_odpoved = input("Zadejte písmeno správné odpovědi:")
            
            if user_odpoved.lower() == otazka["odpoved"].lower():
                print("Správně!")
                vyhra += 10000
                otazky += 1
                vybrane_otazky.append(otazka_index)
            else:
                print("Špatně!")
                break
        
        if vyhra == 100000:
            print("Gratuluji! Vyhrál jste nejvyšší možnou výhru 100 000 $!")
hra()
