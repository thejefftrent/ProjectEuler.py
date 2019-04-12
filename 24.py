#def nth_permutation(x, n):



#print(nth_permutation(10, 1000000), "is it?")

#it's late... can't think... doing this the long way...
#and the very bad way
l = []

#o = [0,1,2,3,4,5,6,7,8,9]
o = [0,1,2]
for os in o:
    o = [0,1,2]
    p = [os]
    o.remove(os)
    for os in o:
        _o = o
        p.append(os)
        o.remove(os)
        for _os in _o:
            p.append(os)
            o.remove(os)
            print(str(p))
