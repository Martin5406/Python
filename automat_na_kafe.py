import os
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

latte = 35
expresso = 25
cokolada = 15
americano = 30
voda = 5

credit = 0


while True:
    clear_terminal()

    print(f"\nA) Latte {latte} Kč"
          f"\nB) Expresso {expresso} Kč"
          f"\nC) Cokolada {cokolada} Kč"
          f"\nD) Americano {americano} Kč" 
          f"\nE) Voda {voda} Kč")
    print(f"\nCredit: {credit} Kč")
    print("\n1 Kč 5 Kč 10 Kč 20 Kč 50 Kč")

    user_input = str(input("\nVložte minci nebo vyberte objednávku nebo 'exit' pro ukončení: "))
    
    if user_input == "1" or user_input == "5" or user_input == "10" or user_input == "20" or user_input == "50":
        credit+=int(user_input)

    elif user_input.lower() == "a":
        if credit >= latte:
            credit-=latte
            print("\nVaše objednávka se připravuje.")
            time.sleep(3)
            print("Vaše objednávka je hotová!")
            time.sleep(3)
        else:
            print("\nNedostanečná kredit!")
            time.sleep(3)

    elif user_input.lower() == "b":
        if credit >= expresso:
            credit-=expresso
            print("\nVaše objednávka se připravuje.")
            time.sleep(3)
            print("Vaše objednávka je hotová!")
            time.sleep(3)
        else:
            print("\nNedostanečná kredit!")
            time.sleep(3)
    
    elif user_input.lower() == "c":
        if credit >= cokolada:
            credit-=cokolada
            print("\nVaše objednávka se připravuje.")
            time.sleep(3)
            print("Vaše objednávka je hotová!")
            time.sleep(3)
        else:
            print("\nNedostanečná kredit!")
            time.sleep(3)
    
    elif user_input.lower() == "d":
        if credit >= americano:
            credit-=americano
            print("\nVaše objednávka se připravuje.")
            time.sleep(3)
            print("Vaše objednávka je hotová!")
            time.sleep(3)
        else:
            print("\nNedostanečná kredit!")
            time.sleep(3)
    
    elif user_input.lower() == "e":
        if credit >= voda:
            credit-=voda
            print("\nVaše objednávka se připravuje.")
            time.sleep(3)
            print("Vaše objednávka je hotová!")
            time.sleep(3)
        else:
            print("\nNedostanečná kredit!")
            time.sleep(3)

    elif user_input.lower() == "exit":
        break

    else:
        print("Nespávný příkaz")
        time.sleep(3)