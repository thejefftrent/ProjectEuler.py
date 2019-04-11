def collatz(x): #make it recursive because yolo
    if x == 1:
        return 1
    if( x % 2 == 0):
        return (collatz(x / 2) + 1)
    else: #it's odd
        return (collatz((3 * x ) + 1) + 1)

def longest_collatz(max):
    long = 0
    for i in range(1, max):
        x = collatz(i)
        if x > long:
            print(i,x)
            long = x
    return long

print(str(collatz(13)))
print(str(longest_collatz(1000000)))