a = [[1,2], [3,4]]

# references are duplicated
b = a[:]

# distinct objects
print( a is b) # False

# contain equivalent values
print( a == b) # True

# these are the same objects
print( a[0] is b[0]) # True

# bind a[0] to a new element
a[0] = [8, 9]

# no longer the same reference
print( a[0] is b[0]) # False

# these are still the same reference
print( a[1] is b[1]) # True

# change the element at a[1]
a[1].append(5)
print(a[1]) # [3, 4, 5]

# uh-oh
print(b[1]) # [3, 4, 5]

print(a) # [[8, 9], [3, 4, 5]]
print(b) # [[1, 2], [3, 4, 5]]
