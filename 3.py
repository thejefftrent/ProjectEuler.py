from helper import is_prime

#This can run for a really long time!
def largest_prime_factor(x):
    lpf = 1
    for i in range(2, int((x/2) + 1)):
        if x % i == 0:
            if is_prime(i):
                print(str(i))
                lpf = i
    return lpf

print(str(largest_prime_factor(600851475143)))