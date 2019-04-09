import math
def is_prime(n):
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