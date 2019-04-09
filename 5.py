from helper import is_prime
def int_list_product(l) -> int:
    if not l:
        return 0
    p = 1
    for i in l:
        p *= i
    return p

def find_factors(x:int) -> list:
    factors = list()
    if is_prime(x):
        factors.append(x)
        return factors
    while int_list_product(factors) <  x:
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                factors.append(i)
            if int_list_product(factors) == x:
                break
    factors.sort()
    return factors


def smallest_multiple(n):
    pro = 1
    for i in range(n-1,1,-1):
        if pro % i != 0:
            print(str(i))
            pro *= i
            print(str(pro))
    return pro

f = find_factors(12)
for i in f:
    print(str(i))