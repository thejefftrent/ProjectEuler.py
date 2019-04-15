tri = []
pent = []
hexa = []

for i in range(100000):
    tri.append(int((i * (i + 1)) / 2))
    pent.append(int((i * ((3 * i) - 1)) / 2))
    hexa.append(i * ((2 * i) - 1))

for t in tri:
    for p in pent:
        if t == p:
            for h in hexa:
                if h == t:
                    print(t)