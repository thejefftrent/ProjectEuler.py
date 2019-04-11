import math
def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def is_palindrome(_s: str):
    #print(_s[:int(len(_s)/2)])
    #print(_s[-int(len(_s)/2):][::-1])
    if len(_s) <= 1:
        return True
    if _s[:int(len(_s)/2)] == _s[-int(len(_s)/2):][::-1]:
        return True
    else:
        return False

def int_list_product(l) -> int:
    if not l:
        return 0
    p = 1
    for i in l:
        p *= i
    return p

def find_prime_factors(x:int) -> list:
    factors = list()
    if is_prime(x):
        factors.append(x)
        return factors
    while int_list_product(factors) <  x:
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                if is_prime(i):
                    factors.append(i)
            if int_list_product(factors) == x:
                break
    factors.sort()
    return factors

def find_factors(x:int) -> list:
    factors = list()
    factors.append(1)
    if is_prime(x):
        factors.append(x)
        return factors
    for i in range(2, int(x/2)+1):
        if x % i == 0:
            factors.append(i)
    factors.append(x)
    return factors