#you might be wondering... do I always think of some of the worse ways you could do somethign? Yes. Yes I do.

d_0 = [0,1,2,3,4,5,6,7,8,9]
ls = []
for d0 in d_0:
    p0 = ""
    d_1 = d_0[:]

    p1 = p0 + str(d0)
    d_1.remove(d0)
    #print(p1)
    for d1 in d_1:
        d_2 = d_1[:]
        p2 = p1 + str(d1)
        d_2.remove(d1)
        #print(p2)
        for d2 in d_2:
            d_3 = d_2[:]
            p3 = p2 + str(d2)
            d_3.remove(d2)
            #print(p3)
            for d3 in d_3:
                d_4 = d_3[:]
                p4 = p3 + str(d3)
                d_4.remove(d3)
                #print(p4)
                for d4 in d_4:
                    d_5 = d_4[:]
                    p5 = p4 + str(d4)
                    d_5.remove(d4)
                    for d5 in d_5:
                        d_6 = d_5[:]
                        p6 = p5 + str(d5)
                        d_6.remove(d5)
                        for d6 in d_6:
                            d_7 = d_6[:]
                            p7 = p6 + str(d6)
                            d_7.remove(d6)
                            for d7 in d_7:
                                d_8 = d_7[:]
                                p8 = p7 + str(d7)
                                d_8.remove(d7)
                                for d8 in d_8:
                                    d_9 = d_8[:]
                                    p9 = p8 + str(d8)
                                    d_9.remove(d8)
                                    p9 += str(d_9[0])
                                    ls.append(p9)
                                    #print(ls)
                                        
            
print(ls[1000000-1])