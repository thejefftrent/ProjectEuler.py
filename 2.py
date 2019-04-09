def sumEvenFib(x):
    a = 1
    b = 1
    s = 0
    while a < x and b < x:
        #print(str(a))
        #print(str(b))
        a = a + b
        b = a + b
        if a % 2 == 0:
            print(str(a))
            s += a
        if b % 2 == 0:
            print(str(b))
            s += b
    return s

print("the sum is",str(sumEvenFib(4000000)))