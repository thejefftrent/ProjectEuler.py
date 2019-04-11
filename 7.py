from helper import is_prime

def nth_prime(n):
    #this is probably bad!
    count = 0
    i = 1
    while True:
        i += 1
        if is_prime(i):
            count += 1
        if(count == n):
            return i

print(str(nth_prime(10001)))