count = 0
for i in range(10000):
    x = i + int(str(i)[::-1])
    for j in range(60):
        if str(x) == str(x)[::-1]:
            print(i,"--",x)
            count += 1
            break
        else:
            x = x + int(str(x)[::-1])
    
print(10000 - count)