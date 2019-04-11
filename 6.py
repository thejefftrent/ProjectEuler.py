def sum_sq_dif(x):
    sum_sq = 0 # the sum of the sqs i.e. 1^2 + 2^2 + 3^2...
    sq_sum = 0 # the sq of the sums i.e. (1 + 2 + 3...)^2

    #calculate sum_sq
    for i in range(1, x+1):
        sum_sq += i**2

    #calculate sq_sum
    for i in range(1, x+1):
        sq_sum += i
    sq_sum = sq_sum ** 2

    return sq_sum - sum_sq

print(str(sum_sq_dif(100)))