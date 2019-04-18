import time
s = time.time()

coins = [1,2,5,10,20,50,100,200]
#coins = [10,20,50,100,200]
coins= coins[::-1]

count = 0
def change(coins, x:int):
    if x < 0:
        return 0
    if x == 0:
        return 1
    count = 0
    c = coins[:]
    for coin in coins:
        count += change(c, x-coin)
        c.remove(coin)
    return count

print(change(coins, 200))

print("--- %s seconds ---" % (time.time() - s))