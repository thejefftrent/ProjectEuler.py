#this logically should work... but oh boy is it not efficient

def lattice_path(lx,ly, x, y):
    if lx == x and ly == y:
        return 1
    subpaths = 0
    if lx < x:
        subpaths += lattice_path(lx+1,ly,x,y)
    if ly < y:
        subpaths += lattice_path(lx,ly+1,x,y)
    return subpaths


# print(str(lattice_path(0,0,1,1)))
# print(str(lattice_path(0,0,2,2)))
# print(str(lattice_path(0,0,3,3)))
# print(str(lattice_path(0,0,4,4)))
# print(str(lattice_path(0,0,5,5)))
# print(str(lattice_path(0,0,6,6)))
# print(str(lattice_path(0,0,7,7)))
# print(str(lattice_path(0,0,8,8)))
# print(str(lattice_path(0,0,9,9)))
# print(str(lattice_path(0,0,10,10)))


#Okay... so I googled the pattern and found that it could be Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2. 

#so let's put that in code
from math import factorial

def binomial_coefficient(n):
    return factorial(2*n) / (factorial(n))**2

print(str(int(binomial_coefficient(20))))

#woowee that was fast