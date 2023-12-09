def binar_decimal(binar):
    decimal = 0
    power = 0
    while binar != 0:
        decimal += (binar % 10) * (2 ** power)
        binar //= 10
        power += 1
    return decimal

def decimal_binar(decimal):
    binar = bin(decimal)[2:]  
    if len(binar) < 8:
        binar = '0' * (8 - len(binar)) + binar
    return binar

def ip_binar_decimal(ip_binar):
    ip_decimal = []
    for i in ip_binar.split('.'):
        decimal = binar_decimal(int(i))
        ip_decimal.append(str(decimal))
    return '.'.join(ip_decimal)

def ip_decimal_binar(ip_decimal):
    ip_binar = []
    for i in ip_decimal.split('.'):
        binar = decimal_binar(int(i))
        ip_binar.append(str(binar))
    return '.'.join(ip_binar)

x = input("Jak chcete IP převádět:\n" "1 - do decimálu\n" "2 - do bináru\n" ":")

if x == "2":
    ip_decimal = input("Zadejte IP adresu v decimálu:")
    ip = ip_decimal_binar(ip_decimal)
    print("IP adresa v binárním formátu:", ip)
else:
    ip_binar = input("Zadejte IP adresu v binárním formátu:")
    ip = ip_binar_decimal(ip_binar)
    print("IP adresa v decimálním formátu:", ip)