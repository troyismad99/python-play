words = "Why sometimes I've believed as many as six impossible things before breakfast.".split()
print(words) # ['Why', 'sometimes', "I've", 'believed', 'as', 'many', 'as', 'six', 'impossible', 'things', 'before', 'breakfast.']

# comprehensions use square brackets
# form is [ expr(item) for item in iterable]
print( [len(word) for word in words]) # [3, 9, 4, 8, 2, 4, 2, 3, 10, 6, 6, 10]

lengths = []
for word in words:
    lengths.append(len(word))

print(lengths) # [3, 9, 4, 8, 2, 4, 2, 3, 10, 6, 6, 10]

from math import factorial

f = [len(str(factorial(x))) for x in range(20)]

# the length of the factorial results for the first 20 digits
print(f) # [1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]
print(type(f)) # <class 'list'>

# sets use {}
# set will remove the duplicate values, but the order is not meaningful

print( {len(str(factorial(x))) for x in range(20)}) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18}

from pprint import pprint as pp

# dictionary also uses {} but uses a :
state_to_capital = {
    'Alaska': 'Juneau',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Maine': 'Augusta',
    'South Carolina': 'Columbia'
} 

# invert dictionary to do lookup in opposite direction

# uses items and tuple unpacking
capital_to_state = {capital: state for state, capital in state_to_capital.items()}

pp(capital_to_state)
'''
{'Atlanta': 'Georgia',
 'Augusta': 'Maine',
 'Columbia': 'South Carolina',
 'Denver': 'Colorado',
 'Honolulu': 'Hawaii',
 'Juneau': 'Alaska',
 'Sacramento': 'California',
 'Tallahassee': 'Florida'}
 '''

# duplicates
words = ['hi', 'hello', 'fox', 'hotel']

# only the last h word is kept
print({x[0] : x for x in words}) # 'h': 'hotel', 'f': 'fox'}

