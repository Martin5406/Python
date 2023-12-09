import random
import json

f = open("otázky.JSON")
data = json.load(f)

otazka = random.randint(data)

print(otazka)