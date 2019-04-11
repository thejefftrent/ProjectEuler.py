from helper import is_prime

#no way this is effecient
def sum_of_prime(x):
    sum = 0
    for i in range(2,x):
        if is_prime(i):
            sum += i
    return sum

print(str(sum_of_prime(2000000)))