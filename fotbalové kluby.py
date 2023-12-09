#Na vstupu vezme výhry, remízy a prohry třech fotbalových klubů a vypíše tabulky s body, které klub nasbíral. 
#Výhra = 3 body, Remíza = 1 bod, Prohra = 0 bodů.

v = int(input("Výhry Varnsdorfu:"))
r = int(input("Remízy Varnsdorfu:"))
p = int(input("Prohry Varnsdorfu:"))

v1 = int(input("Výhry Šluknova:"))
r1 = int(input("Remízy Šluknova:"))
p1 = int(input("Prohry Šluknova:"))

v2 = int(input("Výhry Rumburku:"))
r2 = int(input("Remízy Rumburku:"))
p2 = int(input("Prohry Rumburku:"))

def varnsdorf(v, r, p):
    body = 3*v + r
    return body

def sluknov(v1, r1, p1):
    body = 3*v1 + r1
    return body

def rumburk(v2, r2, p2):
    body = 3*v2 + r2
    return body

body = varnsdorf(v, r, p)
body1 = sluknov(v1, r1, p1)
body2 = rumburk(v2, r2, p2)

if body > body1 and body > body2 and body1 > body2:
    print( "1. Varnsdordf", body,"bodů",
           "\n2. Šluknov",body1,"bodů",
           "\n3. Rumburk", body2,"bodů")
    
elif body > body1 and body > body2 and body2 > body1:
    print( "1. Varnsdordf", body,"bodů",
           "\n2. Rumburk",body2,"bodů",
           "\n3. Šluknov", body1,"bodů")
    
elif body1 > body2 and body > body2:
    print( "1. Šluknov", body1,"bodů",
           "\n2. Varnsord",body,"bodů",
           "\n3. Rumburk", body2,"bodů")
    
elif body1 > body2 and body2 > body:
    print( "1. Šluknov", body1,"bodů",
           "\n2. Rumburk",body2,"bodů",
           "\n3. Varnsdorf", body,"bodů")
    
elif body2 > body and body2 > body1 and body > body1:
    print( "1. Rumburk", body2,"bodů",
           "\n2. Varnsord",body,"bodů",
           "\n3. Šluknov", body1,"bodů")
    
elif body < body1:
    print( "1. Rumburk", body2,"bodů",
           "\n2. Šluknov",body1,"bodů",
           "\n3. Varnsdorf", body,"bodů")   