from helper import is_palindrome
from math import pow

#where x is the number of digits to check, I mean just look at the problem it should make sense.... 
# l_pal_pro(2) should be [91,99] or [99,91]
def l_pal_pro(x):
    #did I mention this is terribly inefficient?
    lpp = 0
    for i in range(10**x,10**(x-1),-1):
        for j in range(10**x,10**(x-1),-1):
            if is_palindrome(str(i*j)):
                if i * j > lpp:
                    lpp = i * j
                #print(i, "*", j, "=", i*j)
    return lpp
print(str(l_pal_pro(3)))