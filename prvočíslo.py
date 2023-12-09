def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True

rozsah1 = int(input("Zadejte nejnižší číslo rozsahu:"))
rozsah2 = int(input("Zadejte nejvyšší číslo rozsahu:"))

count = 0
prvocisla = []
for x in range(rozsah1, rozsah2 + 1):
    if je_prvocislo(x):
        count += 1
        prvocisla.append(x)

if count == 1:
    print("V rozsahu se nachází", count, "prvočíslo.")
    print(*prvocisla, sep = ", ") 
elif count > 1 and count <= 4:
    print("V rozsahu se nachází", count, "prvočísla.")
    print(*prvocisla, sep = ", ") 
elif count == 0:
    print("V rozsahu se nenachází prvočíslo.")
else:
    print("V rozsahu se nachází", count, "prvočíslel.")
    print(*prvocisla, sep = ", ") 