#bagr
b_x = 1
b_y = 3

#krabice
k_x = 2
k_y = 2

pohyb = ["P","D","D","P"]

for i in pohyb:
    if i.upper() == "N":
        b_y +=1
        if b_x == k_x and b_y == k_y:
            k_y +=1
    if i.upper() == "D":
        b_y -=1
        if b_x == k_x and b_y == k_y:
            k_y -=1
    if i.upper() == "P":
        b_x +=1
        if b_x == k_x and b_y == k_y:
            k_x +=1
    if i.upper() == "L":
        b_x -=1
        if b_x == k_x and b_y == k_y:
            k_x -=1

print("Pozice bagru je x:", b_x, "y:", b_y)
print("Pozice krabice je x:", k_x, "y:", k_y)