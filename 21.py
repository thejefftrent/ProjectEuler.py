from helper import int_list_sum, find_proper_factors

def sum_amicable_number(x):
    sum = 0
    for i in range(2,x):
        a = int_list_sum(find_proper_factors(i))
        if a != i:
            b = int_list_sum(find_proper_factors(a))
            if b == i:
                print(a,b)
                sum += a
    return sum
        

print(str(sum_amicable_number(10000)))