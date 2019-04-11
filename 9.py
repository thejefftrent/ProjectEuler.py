def pyth_triplet(x):
    a = 1
    b = 2
    c = 0
    while a + b + c < x:
        while a + b + c < x:
            c = (a**2 + b**2)**0.5
            if c.is_integer():
                print(a,b,c)
                if a + b + c == x:
                    return a * b * c
            b += 1
        a += 1
        b=a+1
        c=b+1
    return -1
                
                

print(str(pyth_triplet(1000)))