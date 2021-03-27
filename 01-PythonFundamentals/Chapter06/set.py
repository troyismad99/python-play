# set -> unordered collection of unique, immutable elements

p = {6, 28, 496, 8128, 35550336}
print(p) # {35550336, 8128, 496, 6, 28}

print(type(p)) # <class 'set'>

# empty set
d = set()
print(d) # set()

# ctor will accept any iterable object and remove duplicates for us
t = [1, 1, 2, 3, 5, 8, 4, 4, 4, 6, 9]
print(t) # [1, 1, 2, 3, 5, 8, 4, 4, 4, 6, 9]

u = set(t)
print(u) # {1, 2, 3, 4, 5, 6, 8, 9}

# membership
print( 3 in u)
print (3 not in u)

# add to a set
u.add(99)
print(u) # {1, 2, 3, 4, 5, 6, 99, 8, 9}

# no error if try and add duplicate
u.add(99)
print(u) # {1, 2, 3, 4, 5, 6, 99, 8, 9}

# use update to add another series
u.update([11, 22, 33])
print(u) # {1, 2, 3, 4, 5, 6, 99, 8, 9, 33, 11, 22}

# remove

# error if not present
u.remove(11)

# no error is not present
u.discard(123)

print(u) # {1, 2, 3, 4, 5, 6, 99, 8, 9, 33, 22}

# shallow copy, copies references
j = u.copy()
k = set(u)

print(u, j, k) 
# {1, 2, 3, 4, 5, 6, 99, 8, 9, 33, 22} 
# {1, 2, 3, 4, 5, 6, 99, 8, 9, 33, 22} 
# {1, 2, 3, 4, 5, 6, 99, 8, 9, 33, 22}}

# algebra operations
blue_eyes = {'Olivia', 'Harry', 'Jack', 'Lily', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc =  {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood =  {'Mia', 'Joshua', 'Lily', 'Oliva'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# blue eyes or blond hair
print(blue_eyes.union(blond_hair)) # {'Olivia', 'Harry', 'Amelia', 'Jack', 'Mia', 'Lily', 'Joshua'}

# blue eyes and blond hair
print(blue_eyes.intersection(blond_hair)) # {'Jack', 'Amelia', 'Harry'}

# blond without blue eyes
print(blond_hair.difference(blue_eyes)) # {'Joshua', 'Mia'}

# blond or blue eyes, but not both
print(blond_hair.symmetric_difference(blue_eyes)) # {'Mia', 'Lily', 'Olivia', 'Joshua'}

# subsets, do all smell HCN have blond hair
print(smell_hcn.issubset(blond_hair)) # True

# can all the people that can smell hcn also taste ptc
print(taste_ptc.issuperset(smell_hcn)) # True

# no members in common
print(a_blood.isdisjoint(o_blood)) # True
