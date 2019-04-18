#from decimal import *
#getcontext().prec = 1000
#print(str(getcontext()))
#print(Decimal(1)/Decimal(7))
sl = 0
bn = 0
for i in range(1000,2,-1):
    if sl > i:
        #print(i+1)
        break
    remainders = []
    for l in range(i):
        remainders.append(0)
    value = 1
    position = 0
    while remainders[value] == 0 and value != 0:
        remainders[value] = position
        value *= 10
        value %= i
        position += 1
    if position - remainders[value] > sl:
        bn = i
        sl = position - remainders[value]

print(sl, bn)