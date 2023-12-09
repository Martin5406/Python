def sifrovani(text, koleje):
    puvodni_text = text.replace(" ", "").lower()
    radek_pocet = len(puvodni_text)
    dvojrozmerne_pole1 = [["*" for _ in range(radek_pocet)] for _ in range(koleje)]

    radek = 0
    direction = 1

    for i in range(radek_pocet):
        dvojrozmerne_pole1[radek][i] = puvodni_text[i]
        if radek == 0:
            direction = 1
        elif radek == koleje - 1:
            direction = -1
        radek += direction

    sifrovany_text = ""

    for i in dvojrozmerne_pole1:
        for j in i:
            if j != "*":
                sifrovany_text += j

    return sifrovany_text

def desifrovani(sifrovany_text, koleje):
    dvojrozmerne_pole1 = [["*" for _ in range(len(sifrovany_text))] for _ in range(koleje)]
    
    radek = 0
    direction = 1
    
    for i in range(len(sifrovany_text)):
        dvojrozmerne_pole1[radek][i] = ""
        if radek == 0:
            direction = 1
        elif radek == koleje - 1:
            direction = -1
        radek += direction
    
    index = 0
    for i in range(koleje):
        for j in range(len(sifrovany_text)):
            if dvojrozmerne_pole1[i][j] == "":
                dvojrozmerne_pole1[i][j] = sifrovany_text[index]
                index += 1
    

    puvodni_text = ""
    radek = 0
    direction = 1
    
    for i in range(len(sifrovany_text)):
        puvodni_text += dvojrozmerne_pole1[radek][i]
        if radek == 0:
            direction = 1
        elif radek == koleje - 1:
            direction = -1
        radek += direction

    return puvodni_text

text = str(input("Zadejte text:"))
koleje = int(input("Zadejte počet kolejí:"))

sifrovany_text = sifrovani(text, koleje)
print(sifrovany_text)

desifrovany_text = desifrovani(sifrovany_text, koleje)
print(desifrovany_text)
