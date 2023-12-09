n = int(input("Zadejte počet loutek:"))
k = int(input("Zadejte maximální nosnost věšáků:"))

vahy = []
for i in range(n):
    vahy.append(int(input(f"Zadejte váhu loutky {i+1}:")))

vahy.sort(reverse = True)

pocet = 0
vesaky = [[]]
for x in vahy:
    if not vesaky or sum(vesaky[-1]) + x > k or len(vesaky[-1]) == 2:
        pocet += 1
        vesaky.append([x])
    else:
        vesaky[-1].append(x)

print("Sára potřebuje",len(vesaky),"věšáků/y")