# tuple is a hetrogeneous immutable sequence
# cannot replace, remove, add elements once created
# delimited by parentheses

# a tuple containing a string, float, and int
t = ("Norway", 4.953, 3)
print(t)

# access an element
print(t[0]) 

print (len(t))

# iterate with for loop
for item in t:
    print(item)
'''
Norway
4.953
3
'''    

# concatenate
print( t + (338, 265e9))
# ('Norway', 4.953, 3, 338, 265000000000.0)

# repitition with * operator
print( t * 3)
# ('Norway', 4.953, 3, 'Norway', 4.953, 3, 'Norway', 4.953, 3)

# nested tuple
a = ((220, 284), (1184, 1210), (2620, 2924), (5020, 5564))

print(a[2])
# (2620, 2924)

# chain together to reach the inner elements
print(a[2][1])
# 2924


# single element tuple requires the trailing comma
k = (391,)

# empty tuple
kk = ()

# optional ()
p = 1, 1, 2, 3, 5, 8, 13, 21
print(p)
# (1, 1, 2, 3, 5, 8, 13, 21)

# multiple return values
def minmax(items):
    return min(items), max(items)

print(minmax([81, 82, 83, 33, 44, 55, 66, 77, 88, 99]))
# (33, 99)

# unpacking
lower, upper = minmax([81, 82, 83, 33, 44, 55, 66, 77, 88, 99])

print(lower, upper)
# 33 99

(a, (b, (c, d))) = (4, (3, (2, 1)))
print(a,b,c,d)
# 4 3 2 1

# swapping two, or more, variables
aa = 'jelly'
bb = 'bean'

print(aa, bb)
# jelly bean

aa, bb = bb, aa

print(aa, bb)
# bean jelly

# ctor
cc = tuple([22, 33, 44, 55, 66])
print(cc)
# (22, 33, 44, 55, 66)

dd = tuple("WayneGretzky")
print (dd)
# ('W', 'a', 'y', 'n', 'e', 'G', 'r', 'e', 't', 'z', 'k', 'y')

# in for containment
print(5 in (3, 5, 17, 257, 65537))
# True

print(5 not in (3, 5, 17, 257, 65537))
# False

