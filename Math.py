import math

def vypocet_obvodu_kruhu(polomer):
    """Vypočítá obvod kruhu."""
    obvod = 2 * math.pi * polomer
    return obvod

def vypocet_obsahu_kruhu(polomer):
    """Vypočítá obsah kruhu."""
    obsah = math.pi * polomer**2
    return obsah

def vypocet_obvodu_trojuhelniku(a, b, c):
    """Vypočítá obvod trojúhelníku."""
    obvod = a + b + c
    return obvod

def vypocet_obsahu_trojuhelniku(zakladna, vyska):
    """Vypočítá obsah trojúhelníku."""
    obsah = 0.5 * zakladna * vyska
    return obsah

def vypocet_obvodu_obdelniku_nebo_ctverce(a, b=None):
    """Vypočítá obvod obdélníku nebo čtverce."""
    if b is None:
        obvod = 4 * a
    else:
        obvod = 2 * (a + b)
    return obvod

def vypocet_obsahu_obdelniku_nebo_ctverce(a, b=None):
    """Vypočítá obsah obdélníku nebo čtverce."""
    if b is None:
        obsah = a**2
    else:
        obsah = a * b
    return obsah

def vypocet_objemu_krychle(a):
    """Vypočítá objem krychle."""
    objem = a**3
    return objem

def vypocet_objemu_kvadru(a, b, c):
    """Vypočítá objem kvádru."""
    objem = a * b * c
    return objem

def vypocet_objemu_kuzele(r, h):
    """Vypočítá objem kužele."""
    objem = (1/3) * math.pi * r**2 * h
    return objem

def vypocet_objemu_jehlanu(a, h):
    """Vypočítá objem jehlanu."""
    objem = (1/3) * a**2 * h
    return objem

def vypocet_kvadraticke_rovnice(a, b, c):
    """Vypočítá řešení kvadratické rovnice."""
    diskriminant = b**2 - 4 * a * c
    if diskriminant > 0:
        x1 = (-b + math.sqrt(diskriminant)) / (2 * a)
        x2 = (-b - math.sqrt(diskriminant)) / (2 * a)
        return x1, x2
    elif diskriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Rovnice nemá reálná řešení."


volba = input("Co chcete vypočítat? Zadejte číslo které odpovídá předvolbě:\n"
              "1 - obvod kruhu\n"
              "2 - obsah kruhu\n"
              "3 - obvod trojúhelníku\n"
              "4 - obsah trojúhelníku\n"
              "5 - obvod obdelníku/čtverce\n"
              "6 - obsah obdelníku/čtverce\n"
              "7 - objem krychle\n"
              "8 - objem kvádru\n"
              "9 - objem kužele\n"
              "10 - objem jehlanu\n"
              "11 - výpočet kvadratické funkce\n"
              "Volba: ")

if volba == '1':
    polomer = float(input("Zadejte poloměr kruhu v cm: "))
    obvod = vypocet_obvodu_kruhu(polomer)
    print("Obvod kruhu je:", obvod, "cm")
elif volba == "2":
    polomer = float(input("Zadejte poloměr kruhu:"))
    obsah0 = vypocet_obsahu_kruhu(polomer)
    print("Obsah kruhu je:", obsah0)
elif volba == "3":
    a = float(input("Zadejte stranu a:"))
    b = float(input("Zadejte stranu b:"))
    c = float(input("Zadejte stranu c:"))
    obvod = vypocet_obvodu_trojuhelniku(a, b, c)
    print("Obvod trojúhelníku je:", obvod)
elif volba == "4":
    zakladna = float(input("Zadejte základnu trojúhelníku:"))
    vyska = float(input("Zadejte základnu výšku trojúhelníku:"))
    obsah = vypocet_obsahu_trojuhelniku(zakladna, vyska)
    print("Obsah trojúhelníku je:", obsah)
elif volba == "5":
    x = str(input("Čeho obvod chcete vypočítat?\n"
                  "1 - čtverec\n"
                  "2 - obdeílník\n"
                  ":"))
    if x == "1":
      a = float(input("Zadejte délku strany čtverce:"))
      obvod = vypocet_obvodu_obdelniku_nebo_ctverce(a, b=None)
      print("Obvod čtverce je:", obvod)
    else:
        a = float(input("Zadejte stranu a:"))
        b = float(input("Zadejte stranu b:"))
        obvod = vypocet_obvodu_obdelniku_nebo_ctverce(a, b)
        print("Obvod obdelníku je:", obvod)
elif volba == "6":
    x = str(input("Čeho obsah chcete vypočítat?\n"
                  "1 - čtverec\n"
                  "2 - obdeílník\n"
                  ":"))
    if x == "1":
      a = float(input("Zadejte délku strany čtverce:"))
      obsah = vypocet_obsahu_obdelniku_nebo_ctverce(a, b=None)
      print("Obsah čtverce je:", obsah)
    else:
        a = float(input("Zadejte stranu a:"))
        b = float(input("Zadejte stranu b:"))
        obsah = vypocet_obsahu_obdelniku_nebo_ctverce(a, b)
        print("Obsah obdelníku je:", obsah)
elif volba == "7":
    a = float(input("Zadejte stranu kryhle:"))
    objem = vypocet_objemu_krychle(a)
    print("Objem krychle je:", objem)
elif volba == "8":
    a = float(input("Zadejte stranu a:"))
    b = float(input("Zadejte stranu b:"))
    c = float(input("Zadejte stranu c:"))
    objem = vypocet_objemu_kvadru(a, b, c)
    print("Objem kvádru je:", objem)
elif volba == "9":
    r = float(input("Zadejte poloměr podstavy kužele:"))
    h = float(input("Zadejte výšku kužele:"))
    objem = vypocet_objemu_kuzele(r, h)
    print("Objem kužele je:", objem)
elif volba == "10":
    a = float(input("Zadejte stranu a podstavy jehlanu:"))
    h = float(input("Zadejte výšku jehlanu:"))
    objem = vypocet_objemu_jehlanu(a, h)
    print("Objem jehlanu je:", objem)
elif volba == "11":
    a = float(input("Zadejte hodnotu a:"))
    b = float(input("Zadejte hodnotu b:"))
    c = float(input("Zadejte hodnotu c:"))
    funkce = vypocet_kvadraticke_rovnice(a, b, c)
    print(funkce)
else:
    print("Tato volba není v nabídce")