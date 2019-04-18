s ="hello"
s = list(s)
s.sort()
print(s)

i = 31
while True:
    i1 = list(str(i))
    i1.sort()
    i2 = list(str(i*2))
    i2.sort()
    i3 = list(str(i*3))
    i3.sort()
    i4 = list(str(i*4))
    i4.sort()
    i5 = list(str(i*5))
    i5.sort()
    i6 = list(str(i*6))
    i6.sort()
    if i1 == i2 and i1 == i3 and i1 == i4 and i1 == i5 and i1 == i6:
        print(i,"--",i1,i2,i3,i4,i5,i6)
    i += 1
    #break