def problem_25(x):
    f1 = 1
    f2 = 1
    i = 2
    while True:
        f1 += f2
        i += 1
        if len(str(f1)) == x:
            break
        f2 += f1
        i += 1
        if len(str(f2)) == x:
            break
    return i
print(str(problem_25(1000)))