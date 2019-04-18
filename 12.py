from helper import factors


#this is bad? maybe my find_factors function isn't very effecient either :thinking:
#this is like really bad... like taking hour + bad
# I looked up some other solutions but didn't understand the math. This will theorhetically work but will take a long time :(
# def highly_divisible_triangular_number(x):
#     i = 0
#     c = 0
#     f = factors(c)
#     while f < x:
#         i += 1
#         c += i
#         f = factors(c)
#         print(f, c)
#     return c

# print(str(highly_divisible_triangular_number(500)))

i = 1
while True:
    trin = int((i * (i + 1)) / 2)
    f = factors(trin)
    #print(trin, f)
    if f >= 500:
        print(trin)
        break
    i += 1
