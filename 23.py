#I am cheating!

import math

def getDivisors(num):
    if num==1:
        return 1
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while (divisor < n):
        if (num%divisor == 0):
            total += divisor
            total += num//divisor
        divisor+=1
    if n**2==num:
        total+=n
    return total

def isAbundant(num):
    if (getDivisors(num) > num):
        return True
    else:
        return False

abundentNums = []
for x in range (0,28124):
    if (isAbundant(x)):
        abundentNums.append(x)
del abundentNums[0]

sums = [0]*28124
for x in range (0, len(abundentNums)):
    for y in range (x, len(abundentNums)):
            sumOf2AbundantNums = abundentNums[x]+abundentNums[y]
            if (sumOf2AbundantNums<= 28123):
                if (sums[sumOf2AbundantNums] == 0):
                    sums[sumOf2AbundantNums] = sumOf2AbundantNums

total = 0
for x in range (1,len(sums)):
    if (sums[x] == 0):
        total +=x

print('\n', total)








#WOW this takes forever... you must be really proud of yourself!


from helper import find_proper_factors, int_list_sum

#print(find_proper_factors(12))

ab = []
for i in range(2, 28124):
    f = find_proper_factors(i)
    s = int_list_sum(f)
    if s > i:
        ab.append(i)

s = 0
ls = []
for a in ab:
    for b in ab:
        if (a+b) not in ls and a + b <= 28123:
            #print(a,b,a+b)
            ls.append(a+b) 
    print(a)
print(ls)
for i in range(28124):
    if i not in ls:
        s += i