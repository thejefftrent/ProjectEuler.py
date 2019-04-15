from math import factorial
i = 3
_s = 0
while True:
    s = 0
    for _d in str(i):
        d = int(_d)
        s += factorial(d)
    if s == i:
        _s += i
        print(_s,i)
    i += 1


