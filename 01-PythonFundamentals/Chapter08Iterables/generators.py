# needs at least one yield statement
def gen123():
    yield 1
    yield 2
    yield 3

# returns an iterator
a = gen123()
print(next(a)) # 1
print(next(a)) # 2
print(next(a)) # 3
#print(next(a)) # StopIteration exception

for v in gen123():
    print(v)

def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")

g = gen246()
print(next(g))
# About to yield 2
# 2

print(next(g))
# About to yield 4
# 4

print(next(g))
# About to yield 6
# 6

# print(next(g))
'''
About to return
Traceback (most recent call last):
  File "/Users/troy/Development/Python/python-play/01-PythonFundamentals/Chapter08Iterables/generators.py", line 39, in <module>
    print(next(g))
StopIteration
'''

# stateful generators
def take(count, iterable):
    """Take items from the front of an iterable."""

    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        # each iteration causes an execution of take to retrieve the next value
        print(item)

run_take()
'''
2
4
6
'''


# Laziness and the Infinite


# all squares for the first million numbers
million_squares = (x*x for x in range(1,1000001))

# at this point just a generator
print(type(million_squares)) # <class 'generator'>

# actual list would be about 40MB for list and the million integers
# print(list(million_squares))

# sum of first ten million squares
print(sum(x*x for x in range(1,10000001))) # 333333383333335000000
# with a list memory usage is 400MB
# the generator memory is insignificant


# "Batteries included" Iteration tools
# see itertools module


import itertools
import math

def is_prime(x):
    
    if x < 2:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True

# find the sum of the first 1000 primes

# generator to get the first 1000 primes
thousand_primes = itertools.islice(( x for x in itertools.count() if is_prime(x)), 1000)

print(list(thousand_primes)) # [2, 3, 5, 7, .... 7901, 7907, 7919]

# need to recreate the generator
print(sum(itertools.islice(( x for x in itertools.count() if is_prime(x)), 1000))) # 3682913


# any and all 
# 
# equivalent to and and or, but for iterable series
print( any([False, False, True])) # True
print( all([False, False, True])) # False

# are there any primes in this range?
print(any(is_prime(x) for x in range(1328, 1361))) # False


# zip - syncronize iterations over two iterable series

# temperature data
sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]

# combine into pairs of readings
for item in zip(sunday, monday):
    print(item)

'''
(12, 13)
(14, 14)
(15, 14)
(15, 14)
(17, 16)
(21, 20)
(22, 21)
(22, 22)
(23, 22)
(22, 21)
(20, 19)
(18, 17)
'''
# since it yields a tuple we can unpack
for sun , mon in zip(sunday, monday):
    print("average=", (sun + mon) / 2)
'''
average= 12.5
average= 14.0
average= 14.5
average= 14.5
average= 16.5
average= 20.5
average= 21.5
average= 22.0
average= 22.5
average= 21.5
average= 19.5
average= 17.5
'''

temperatures = itertools.chain(sunday, monday)

# are all temps above freezing
print(all(t > 0 for t in temperatures))


