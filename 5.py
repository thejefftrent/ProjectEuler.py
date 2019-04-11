from helper import is_prime, find_prime_factors, int_list_product

def smallest_multiple(n):
    ls = list()

    for i in range(2,n):
        pf = find_prime_factors(i)
        for l in ls:
            for f in pf:
                if(l == f):
                    pf.remove(f)
                    break
        for f in pf:
            ls.append(f)
        ls.sort()


    return int_list_product(ls)


print(str(smallest_multiple(20)))