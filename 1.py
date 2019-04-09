def multiplesOf3And5(x):
    sum = 0
    for i in range(x):
        #print(str(i))
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(str(multiplesOf3And5(10)))