from termcolor import colored
import random
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()

def zivoty_draka():
    while True:
        drak = random.randint(50,100)
        if drak % 10 == 0:
            return drak

mista = []
drak_zivoty = zivoty_draka()

def konec_hry(zivoty):
    if zivoty <= 0:
        return colored("\nDOŠLI TI ŽIVOTY, KONEC HRY!","red")

print("\nJseš v lese a našel si mapu k pokladu!"
      "\nTvůj úkol je najít poklad."
      "\nMusíš však dávat pozor na tvoje živoy, pokud o všechny příjdeš hra končí!")

zivoty = 100

input(colored("\nStiskni Enter pro pokračování...","yellow"))
clear_terminal()

while True:
    print(colored(f"\nTvoje životy {zivoty}.","green"))
    print("\nJdeš podle mapy a narazíš na první překážku."
        "\nBuď půjdeš kratší cestou, které ale vypadá nebezpečně."
        "\nNebo půjdeš klidnou cestou, která je ale delší a neznáš ji.")

    input(colored("\nStiskni Enter pro pokračování...","yellow"))
    print("\nMožnost 1: Kratší cesta"
        "\nMožnost 2: Delší cesta")


    moznost = int(input("Zvol si cestu (1 nebo 2):"))
    if moznost == 1:
        clear_terminal()
        print("\nŠel si kratší cestou a jako zázrakem se ti nic nestalo.")
        print(colored(f"\nTvoje životy {zivoty}.","green"))
        input(colored("\nStiskni Enter pro pokračování...","yellow"))
        clear_terminal()
        break
    elif moznost == 2:
        clear_terminal()
        print("\nŠel si delší cestou a ztratil se."
            "\nPo neznámé cestě si potkal vlka, který ti ubral 20 životů!")
        
        zivoty -=20

        print(colored(f"\nTvoje životy {zivoty}.","green"))

        input(colored("\nStiskni Enter pro pokračování...","yellow"))
        clear_terminal()
        break
    else:
        clear_terminal()
        print("\nNezadali jste volbu podle předvolby.")

if zivoty <=0:
    print(konec_hry(zivoty))
    exit()
else:
    while True:
        if zivoty < 0:
            print(konec_hry(zivoty))
            break
        else:
            print("\nPokračuješ dál lesem."
                "\nNyní ses dostal do jeskyně."
                "\nNic ale nevidíš, avšak máš možnost si vyrobit louči.")
            
            input(colored("\nStiskni Enter pro pokračování...","yellow"))
            
            print("\nMožnost 1: Vyrobit louč"
                "\nMožnost 2: Jít jeskyní po tmě")
        
            moznost2 = int(input("Zvol si možnost (1 nebo 2):"))
            if moznost2 == 1:
                clear_terminal()
                print("\nPři výrobě louče si se poranil a ubralo ti to 10 životů!"
                    "\nAvšak nyní vidíš na cestu a úspěšně se dostaneš z jeskyně!")
                
                zivoty -=10
                print(colored(f"\nTvoje životy {zivoty}.","green"))
                input(colored("\nStiskni Enter pro pokračování...","yellow"))
                clear_terminal()
                break
            elif moznost2 == 2:
                clear_terminal()
                print("\nJdeš jeskyní po tmě, a jelikož nevidíš spadl si do jámy!"
                    "\nJsi v ní zaseklý a pád ti ubral 25 životů!")
                
                zivoty -= 25
                print(colored(f"\nTvoje životy {zivoty}.","green"))
                input(colored("\nStiskni Enter pro pokračování...","yellow"))
                clear_terminal()
                print("\nV jámě je díra, do které můžeš vlézt, nevíš kam vede."
                        "\nJe tu i možnost čekat jestli se neobjeví někdo, kdo by tě osvobodil.")
                
                input(colored("\nStiskni Enter pro pokračování...","yellow"))
                print("\nMožnost 1: Vlézt do díry"
                "\nMožnost 2: Čekat")

                while True:
                    moznost3 = int(input("Zvol si možnost (1 nebo 2):"))

                    if moznost3 == 1:
                        clear_terminal()
                        print("\nVlezl si do díry, a podařilo se ti dostan ven!"
                            "\nAle díra byla moc úzká a ubrala ti 15 životů.")
                        zivoty -=15
                        print(colored(f"\nTvoje životy {zivoty}.","green"))
                        input(colored("\nStiskni Enter pro pokračování...","yellow"))
                        clear_terminal()
                        break
                    elif moznost3 == 2:
                        clear_terminal()
                        print("\nPo hodinách čekání se nikdo neobjevil, a tak si stejně do díry vlez."
                            "\nAle díra bylo moc úzká a ubrala ti životy."
                            "\nJelikož si byl vyčerpaný, trvalo ti to dlouho a ubralo ti to 25 životů.")
                        zivoty -=25
                        print(colored(f"\nTvoje životy {zivoty}.","green"))
                        input(colored("\nStiskni Enter pro pokračování...","yellow"))
                        clear_terminal()
                        break
                    else:
                        print("\nNezadali jste volbu podle předvolby.")
                break     
            else:
                clear_terminal()
                print("\nNezadali jste volbu podle předvoloby.")

if zivoty <=0:
    print(konec_hry(zivoty))
    exit()
else:
    while True:
        print("\nDál v mapě neumíš číst, proto musíš najít mága, který v mapě číst umí."
            "\nUž si na konci lesa, a potřebuješ se dostat do vesnice za mágem."
            "\nPotkáš muže, kterého se zeptáš na cestu."
            "\nMuž však vypadá podezřele a nevíš, jestli mu věřit."
            "\nPoradil ti že máš jít do leva. Poslechneš ho?")

        input(colored("\nStiskni Enter pro pokračování...","yellow"))
        print("\nMožnost 1: Jít do leva (cesta kterou ti poradil muž)"
            "\nMožnost 2: Jít do prava")
        
        moznost3 = int(input("Zvol si možnost (1 nebo 2):"))

        if moznost3 == 1:
            clear_terminal()
            print("\nŠel si cestou, kterou ti poradil muž."
                  "\nNa cestě na tebe čekali lapkové, kteří tě okradli a ubrali ti 60 životů!")
            
            zivoty -= 60

            print(colored(f"\nTvoje životy {zivoty}.","green"))
            input(colored("\nStiskni Enter pro pokračování...","yellow"))
            clear_terminal()
            break
        elif moznost3 == 2:
            clear_terminal()
            print("\nŠel si do prava a našel vesnici."
                "\nMuž ti poradil špatně.")
            
            print(colored(f"\nTvoje životy {zivoty}.","green"))
            input(colored("\nStiskni Enter pro pokračování...","yellow"))
            clear_terminal()
            break
        else:
            clear_terminal()
            print("\nNezadali jste volbu podle předvolby.")

if zivoty <=0:
    print(konec_hry(zivoty))
    exit()
else:
    print("\nPovedlo se ti dostat do vesnice a nevíš kde najít mága."
        "\nMáš několit možností kam se vydat.")
                
    while True:
        input(colored("\nStiskni Enter pro pokračování...","yellow"))
        clear_terminal()
        print("\nMožnost 1: Jít se zeptat do hospody"
            "\nMožnost 2: Jít se zeptat ke kováři"
            "\nMožnost 3: Jít se zeptat kněze"
            "\nMožnost 4: Jít se zeptat rychtáře")
        
        moznost4 = int(input("Zvol si možnost (1-4):"))
        mag = False

        if moznost4 == 1:
            if 1 in mista:
                clear_terminal()
                print("\nV hospodě jsi už byl.")
            else:
                clear_terminal()
                print("\nV hospodě je muž, který ti řekne, kde je mág, pokud ho porazíš v páce."
                    "\nPřijmeš výzvu ?")
                input(colored("\nStiskni Enter pro pokračování...","yellow"))
                while True:
                    paka = int(input("\nMožnost 1: Ano"
                                    "\nMožnost 2: Ne"
                                    "\nZvol si možnost (1 nebo 2):"))
                    if paka == 1:
                        clear_terminal()
                        print("\nPřijal si výzvu a musíš porazit muže.")
                        input(colored("\nStiskněte Enter pro pokračování...", "yellow"))
                        clear_terminal()
                        sance = random.randint(1, 2)
                        if sance == 1:
                            print("\nPorazil si muže v páce!"
                                  "\nAle ubralo ti to 10 životů!"
                                "\nŘekl ti, že mág se nachází za vesnicí u řeky.")

                            zivoty -= 10
                            print(colored(f"\nTvoje životy {zivoty}.","green"))
                            mag = True
                            input(colored("\nStiskni Enter pro pokračování...","yellow"))
                            clear_terminal()
                            break
                        else:
                            print("\nBohužel tě muž porazil a musíš se poptat jinde."
                                  "Navíc ti ubral 20 životů!")
                            zivoty -=20
                            print(colored(f"\nTvoje životy {zivoty}.","green"))
                            mista.append(1)
                            if zivoty <=0:
                                print(konec_hry(zivoty))
                                exit()
                            else:
                                break
                    elif paka == 2:
                        clear_terminal()
                        print("\nPáku si odmítnul."
                            "\nV hospodě si nic nezjistil.")
                        mista.append(1)
                        break
                    else:
                        clear_terminal()
                        print("\nNezadali jste volbu podle předvolby.")
        elif moznost4 == 2:
            if 2 in mista:
                clear_terminal()
                print("Kovář už ti neporadí.")
            else:
                clear_terminal()
                print("\nKovář je ochotný ti říct, kde je mág pokud mu pomůžeš.")
                print("Chce aby si ukradl rukojeť, kterou mu obchodník nechce prodat."
                    "\nPomůžeš mu?")
                input(colored("\nStiskni Enter pro pokračování...","yellow"))

                while True:
                    kradez = int(input("\nMožnost 1: Ano"
                                    "\nMožnost 2: Ne"
                                    "\nZvol si možnost (1 nebo 2):"))
                    if kradez == 1:
                        clear_terminal()
                        print("\nJdeš ukrást obchoníkovi rukojeť.")
                        sance1 = random.randint(1,4)
                        input(colored("\nStiskni Enter pro pokračování...","yellow"))
                        clear_terminal()
                        if sance1 == 1:
                            print("\nPodařilo se ti ukrást rukojeť!"
                                  "\nKovář ti řekl, že mág se nachází za vesnicí u řeky.")
                            mag = True
                            input(colored("\nStiskni Enter pro pokračování...","yellow"))
                            clear_terminal()
                            break
                        else:
                            clear_terminal()
                            print("Nepodařilo se ti ukrást rukojeť."
                                "Obchodník ti navíc ubral 30 životů!")
                            mista.append(2)
                            zivoty -=30
                            print(colored(f"\nTvoje životy {zivoty}.","green"))
                            if zivoty <=0:
                                print(konec_hry(zivoty))
                                exit()
                            else:
                                break
                    elif kradez == 2:
                        clear_terminal()
                        print("\nOdmítl si."
                            "\nOd kováře si nic nezjistil.")
                        mista.append(2)
                        break
                    else:
                        print("\nNezadali jste volbu podle předvolby.")
        elif moznost4 == 3:
            clear_terminal()
            print("\nZašel si za knězem."
                  "\nKněz ti ochtoně poradí."
                   "\nMág se nachází za vesnicí u řeky.")
            mag = True
            input(colored("\nStiskni Enter pro pokračování...","yellow"))
            clear_terminal()
            break
        elif moznost4 == 4:
            if 4 in mista:
                clear_terminal()
                print("\nRychtář nic neví.")
            else:
                clear_terminal()
                print("\nZašel si za rychtářem."
                    "\nRychtář tvrdí, že žádného mága nezná."
                    "\nNic si nezjistil")
                mista.append(4)
        else:
            clear_terminal()
            print("\nNezadali jste volbu podle předvolby.")
        
        if mag == True:
            break

            
if zivoty <=0:
    print(konec_hry(zivoty))
    exit()
else:
    print("\nPovedlo se ti najít mága."
            "\nViděl, že jsi zraněný, a tak ti dal lektvar, který ti přidal 2 životy!")

    zivoty +=2

    print(colored(f"\nTvoje životy {zivoty}.","green"))
    input(colored("\nStiskni Enter pro pokračování...","yellow"))
    clear_terminal()

    print("\nMág z mapy vyčte, že poklad se nachází na vrchulu hory za vesnicí."
            "\nOkamžitě se vydáš nahoru.")
    
    input(colored("\nStiskni Enter pro pokračování...","yellow"))
    clear_terminal()

    print("\nKdyž se dostaneš nahoru zjistíš, že poklad hlídá drak."
            "\nMusíš draka porazit, aby si mohl poklad získat."
            "\nNa útok máš meč, který je pro odvážlivce, kteří se s drakem hodlají utkat.")

    input(colored("\nStiskni Enter pro pokračování...","yellow"))
    clear_terminal()

    print("\nDrakovi útoky mohou ubírat v rozmezí 1-10."
          "\nTvoje útoky mohou ubírat v rozmezí 1-15.")
    
    print(colored(f"\nŽivoty draka: {drak_zivoty}","red"))
    print(colored(f"Tvoje životy: {zivoty}","green"))

    print("\nAbys draka porazil, musíš mu ubrat všechny životy."
          "\nBoj začal!")
    
    input(colored("\nStiskni Enter pro pokračování...","yellow"))
    clear_terminal()

    while drak_zivoty > 0 and zivoty > 0:
        if zivoty > 0:
            utok_hrace = random.randint(1, 15)
            drak_zivoty -= utok_hrace
        if drak_zivoty > 0:
            utok_drak = random.randint(1, 10)
            zivoty -= utok_drak

        print(colored(f"\nÚtok draka: {utok_drak}", "red"))
        print(colored(f"Tvůj útok: {utok_hrace}", "green"))

        print(colored(f"\nŽivoty draka: {drak_zivoty}", "red"))
        print(colored(f"Tvoje životy: {zivoty}", "green"))

        if drak_zivoty <= 0:
            print(colored("\nGratuluji, porazil jsi draka!"
                  "\nNyní je poklad tvůj!","green"))
            exit()
        elif zivoty <= 0:
            print(colored("\nBohužel, drak tě porazil. HRA KONČÍ!"
                  "\nPoklad se ti nepodařilo získat.", "red"))
            exit()
            
        input(colored("\nStiskni Enter pro pokračování...","yellow"))
        clear_terminal()