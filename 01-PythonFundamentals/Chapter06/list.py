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
