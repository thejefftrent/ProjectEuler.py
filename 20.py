#another one this is probably made easy by python being flexible

from math import factorial

x = factorial(100)

sum = 0
for n in str(x):
    sum += int(n)

print(str(sum))
