#Na vstup bere výšku a váha, následně vypočíta BMI.

vaha = int(input("Zadej váhu v kg:"))
vyska = int(input("Zadej výšku v cm:"))

vyska /= 100
bmi = vaha/(vyska**2)

print(bmi)
if (bmi < 18.5):
    print("Máš podváhu.")
elif(bmi < 24.9):
    print("Nemáš ani podváhu ani nadváhu.")
else:
    print("Máš nadváhu.")


