with open('p022_names.txt','r') as file:
    names = file.read()
names = names.replace('"','').split(',')

#for i in range(len(names)):
#    print(names[i])
#    names[i] = names[i].strip('"')

# -64
names.sort()
sum = 0
for i in range(len(names)):
    name = 0
    for c in names[i]:
        name += (ord(c) - 64)
    sum += name * (i + 1)
print("total is",sum)