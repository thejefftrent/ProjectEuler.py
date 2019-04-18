from helper import is_prime

def zero_to_infinity():
    i = 0
    while True:
        yield i
        i += 1



def r_q(n,a,b):
    return ((n**2) + (a * n) + b)

hi_n = 0
hi_co = 0 
for a in range(-1000,1001):
    #print(a,hi_n,hi_co)
    for b in range(-1000, 1001):
        for n in zero_to_infinity():
            if not is_prime(r_q(n,a,b)):
                break
            else:
                if n > hi_n:
                    hi_n = n
                    if hi_co != [a,b]:
                        hi_co = [a,b]
                    
print(hi_co, hi_co[0] * hi_co[1], hi_n)

