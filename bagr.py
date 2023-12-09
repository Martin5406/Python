bagr_x = 1
bagr_y = 3

krabice_x = 2
krabice_y = 2

print(f"Pozice bagru: x: {bagr_x} y: {bagr_y}")
print(f"Pozice krabice: x: {krabice_x} y: {krabice_y}")
pohyb = str(input("Zadejte pohyb bagru:"))

for i in pohyb:
    if i.upper() == 'N':
        bagr_y += 1
        if bagr_x == krabice_x and bagr_y == krabice_y:
            krabice_y += 1
    elif i.upper() == 'P':
        bagr_x += 1
        if bagr_x == krabice_x and bagr_y == krabice_y:
            krabice_x += 1
    elif i.upper() == 'D':
        bagr_y -= 1
        if bagr_x == krabice_x and bagr_y == krabice_y:
           krabice_y -= 1
    elif i.upper() == 'L':
        bagr_x -= 1
        if bagr_x == krabice_x and bagr_y == krabice_y:
                krabice_x -= 1

print(f"Pozice bagru: {bagr_x} {bagr_y}")
print(f"Pozice krabice: {krabice_x} {krabice_y}")


