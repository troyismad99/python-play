#list  - hetrogeneous mutable sequence

# create a list from a string
s = "show how to index into sequences".split()
print(s)
#['show', 'how', 'to', 'index', 'into', 'sequences']

'''
       ['show', 'how', 'to', 'index', 'into', 'sequences']
indexes  0       1      2     3        4       5
        -6,-0   -5     -4    -3       -2      -1
'''

# fifth element from start
print(s[4]) # into

# third index from end
print(s[-3]) # index

print(s[-0]) # show
print(s[-6]) # show

# slicing to extract part of a list
print(s[1:4]) # ['how', 'to', 'index']

# all elements but first and last
print(s[1:-1]) # 'how', 'to', 'index', 'into']

# Slice args are optional
# all from third to end
print(s[3:]) # ['index', 'into', 'sequences']
print(s[:3]) # ['show', 'how', 'to']

# Copying a list
full_slice = s[:]
print(full_slice) # ['show', 'how', 'to', 'index', 'into', 'sequences']

print(full_slice is s) # False
print(full_slice == s) # True

u = s.copy()

# list ctor preferred
v = list(s)
print(v) # ['show', 'how', 'to', 'index', 'into', 'sequences']

# repitition
c = [21, 37]
d = c * 4
print(d) # [21, 37, 21, 37, 21, 37, 21, 37]

# mostly for initialization
print([0] * 9) # [0, 0, 0, 0, 0, 0, 0, 0, 0]

# also a shallow copy (it repeats the reference, not the value)
s = [[-1, +1]] * 5
print(s) # [-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 1]]

s[3].append(7)
print(s) # [[-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7]]


#searching
w = "The quick brown fox jumps over the lazy dog".split()

i = w.index('fox')
print(i)    # 3
print(w[i]) # fox

#w.index('unicorn')
'''
Traceback (most recent call last):
  File "/Users/troy/Development/Python/python-play/01-PythonFundamentals/Chapter06/list.py", line 70, in <module>
    w.index('unicorn')
ValueError: 'unicorn' is not in list
'''

w.count('the') # 2

# membership
print( 'fox' in w)     # True
print( 'fox' not in w) # False

# remove from list
del w[3]
print(w) #['The', 'quick', 'brown', 'jumps', 'over', 'the', 'lazy', 'dog']

w.remove('lazy')
print(w) # ['The', 'quick', 'brown', 'jumps', 'over', 'the', 'dog']

# insert
w.insert(3, 'fox')
print(w) # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'dog']

# back to a string
print(' '.join(w)) # The quick brown fox jumps over the dog

# concatenate
m = [2, 1, 3]
n = [4, 7, 11]
k = m + n
print(k) # 2, 1, 3, 4, 7, 11]

k += [18, 29, 47]
print(k) # [2, 1, 3, 4, 7, 11, 18, 29, 47]

k.extend([76, 129, 199])
print(k) # [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 129, 199]

# reversing and sorting
k.reverse()
print(k) #[199, 129, 76, 47, 29, 18, 11, 7, 4, 3, 1, 2]

k.sort()
print(k) # [1, 2, 3, 4, 7, 11, 18, 29, 47, 76, 129, 199]

k.sort(reverse=True)
print(k) # [199, 129, 76, 47, 29, 18, 11, 7, 4, 3, 2, 1]

# sort by key
w = "The quick brown fox jumps over the lazy dog".split()
w.sort(key=len)
print(' '.join(w)) # The fox the dog over lazy quick brown jumps

# 
x = [4, 9, 2, 1]

# return a new list of x that is sorted
y = sorted(x)

print(x) # 4, 9, 2, 1]
print(y) # [1, 2, 4, 9]

# returns an interator
z = reversed(x) 
# print(z) # <list_reverseiterator object at 0x100dfcf10>

print(list(z)) # [1, 2, 9, 4]


