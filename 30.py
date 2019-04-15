from time import sleep
i = 2
while True:
    #print(str(i))
    s = 0
    for _d in str(i):
        d = int(_d)
        s += d**5
        #print(str(d**5))
    #print(str(s))
    #sleep(1)
    if i == s:
        print(str(i))
    i += 1
