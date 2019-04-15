
l = []
for i in range(2, 101):
    for j in range(2,101):
        l.append(i**j)
l = list(dict.fromkeys(l))
print(str(len(l)))