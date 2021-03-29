from pprint import pprint as pp
from math import sqrt

def is_prime(x):
    
    if x < 2:
        return False
    
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True

# filtering format: [ expr(item) for item in iterable if predicate(item)]

# all primes up to 100
print( [x for x in range(101) if is_prime(x)] )
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# dictionay of numbers with exactly three divisors matched to a tuple of those divisors
prime_square_divisors = {x*x:(1, x, x*x) for x in range(101) if is_prime(x)}

pp(prime_square_divisors)
'''
{4: (1, 2, 4),
 9: (1, 3, 9),
 25: (1, 5, 25),
 49: (1, 7, 49),
 121: (1, 11, 121),
 169: (1, 13, 169),
 289: (1, 17, 289),
 361: (1, 19, 361),
 529: (1, 23, 529),
 841: (1, 29, 841),
 961: (1, 31, 961),
 1369: (1, 37, 1369),
 1681: (1, 41, 1681),
 1849: (1, 43, 1849),
 2209: (1, 47, 2209),
 2809: (1, 53, 2809),
 3481: (1, 59, 3481),
 3721: (1, 61, 3721),
 4489: (1, 67, 4489),
 5041: (1, 71, 5041),
 5329: (1, 73, 5329),
 6241: (1, 79, 6241),
 6889: (1, 83, 6889),
 7921: (1, 89, 7921),
 9409: (1, 97, 9409)}
 '''


