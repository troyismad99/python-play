# dict - unordered mapping from unique, immutable keys to mutable values

a = {'a': 'aaa',
     'b': 'bbb',
     'c': 'ccc',
     'd': 'ddd'}

print(a) # {'a': 'aaa', 'b': 'bbb', 'c': 'ccc', 'd': 'ddd'}

print(a['b']) # bbb

# can convert into a dictionary
# list of tuples
t = [("Alice", 11), ("Bob", 22), ("Chuck", 33), ("Dean", 44) ]
print(t) # [('Alice', 11), ('Bob', 22), ('Chuck', 33), ('Dean', 44)]

d = dict(t)
print(d) # {'Alice': 11, 'Bob': 22, 'Chuck': 33, 'Dean': 44}

# shallow copies
e = d.copy()
f = dict(d)

# extend 
g = dict(Edgar=55)

d.update(g)
print(d) # {'Alice': 11, 'Bob': 22, 'Chuck': 33, 'Dean': 44, 'Edgar': 55}

# iterable
# keys returned in arbitrary order
for key in d:
    print("{key} => {value}".format(key=key, value=d[key]))

'''
Alice => 11
Bob => 22
Chuck => 33
Dean => 44
Edgar => 55
'''

# each dictionary items is a tuple, use tuple unpacking 
for key, value in d.items():
    print("{key} => {value}".format(key=key, value=value))

from pprint import pprint as pp
pp(d)
#{'Alice': 11, 'Bob': 22, 'Chuck': 33, 'Dean': 44, 'Edgar': 55}

