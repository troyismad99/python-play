# strings
'''
>>> help(str)
>>> c = 'oslo'
>>> c.capitalize() # note that c doesn't change
'Oslo'
>>> print(c)
oslo
'''

a = "Mixed quotes allow for ' inside"
print(a)

b = 'Another example of a double " in a string'
print(b)

c = 'The escape char is a back slash. Use for newline \n and a single quote \' or a \\' 
print(c)

e = r'Lower r is the literal operator. Will ignore all escape chars so one \ is ok'
print(e)


# bytes
# immutable sequences of bytes
# use the b
e = b'some bytes'
print(e.split())

# http reponses are byte

# lists
f = [1, 2, 3]
g = ["apple", "orange", "pear"]

print(g[1])

g[1] = 7 # can mix types in a list
print(g)

h = [] # create empty list

i = list("characters") # ctor - create list from a string
print(i)

j = ['one',
     'two',
     'three',] # note pyhton is cool and the gang with the extra comma
print(j)

# Dict -> dictionaries 
# keys and values
k = {'alice': '878-123-1234', 'bob': '123-123-1234', 'eve': '123-456-7890'}
print(k)

print(k['alice'])

k['charles'] = '123-555-4567' # will create a new entry
print(k)

# for loops (foreach in other languages)
cities = ["London", "New York", "Paris"]
for city in cities:
    print(city)

# for dict we get the keys
for n in k:
    print(n, k[n])


'''
#repl

>>> from urllib.request import urlopen
>>> with urlopen('http://sixty-north.com/c/t.txt') as story:
...     story_words = []
...     for line in story:
...         line_words = line.split()
...         for word in line_words:
...             story_words.append(word)
... 
>>> story_words
[b'It', b'was', b'the', b'best', b'of', b'times', b'it', b'was', b'the', b'worst', b'of', b'times', b'it', b'was', b'the', b'age', b'of', b'wisdom', b'it', b'was', b'the', b'age', b'of', b'foolishness', b'it', b'was', b'the', b'epoch', b'of', b'belief', b'it', b'was', b'the', b'epoch', b'of', b'incredulity', b'it', b'was', b'the', b'season', b'of', b'Light', b'it', b'was', b'the', b'season', b'of', b'Darkness', b'it', b'was', b'the', b'spring', b'of', b'hope', b'it', b'was', b'the', b'winter', b'of', b'despair', b'we', b'had', b'everything', b'before', b'us', b'we', b'had', b'nothing', b'before', b'us', b'we', b'were', b'all', b'going', b'direct', b'to', b'Heaven', b'we', b'were', b'all', b'going', b'direct', b'the', b'other', b'way', b'in', b'short', b'the', b'period', b'was', b'so', b'far', b'like', b'the', b'present', b'period', b'that', b'some', b'of', b'its', b'noisiest', b'authorities', b'insisted', b'on', b'its', b'being', b'received', b'for', b'good', b'or', b'for', b'evil', b'in', b'the', b'superlative', b'degree', b'of', b'comparison', b'only']

# note these are byte objects
# to make into strings use the decode when splitting

>>> with urlopen('http://sixty-north.com/c/t.txt') as story:
...     story_words = []
...     for line in story:
...         line_words = line.decode('UTF-8').split()
...         for word in line_words:
...             story_words.append(word)
... 
>>> story_words
['It', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness', 'it', 'was', 'the', 'epoch', 'of', 'belief', 'it', 'was', 'the', 'epoch', 'of', 'incredulity', 'it', 'was', 'the', 'season', 'of', 'Light', 'it', 'was', 'the', 'season', 'of', 'Darkness', 'it', 'was', 'the', 'spring', 'of', 'hope', 'it', 'was', 'the', 'winter', 'of', 'despair', 'we', 'had', 'everything', 'before', 'us', 'we', 'had', 'nothing', 'before', 'us', 'we', 'were', 'all', 'going', 'direct', 'to', 'Heaven', 'we', 'were', 'all', 'going', 'direct', 'the', 'other', 'way', 'in', 'short', 'the', 'period', 'was', 'so', 'far', 'like', 'the', 'present', 'period', 'that', 'some', 'of', 'its', 'noisiest', 'authorities', 'insisted', 'on', 'its', 'being', 'received', 'for', 'good', 'or', 'for', 'evil', 'in', 'the', 'superlative', 'degree', 'of', 'comparison', 'only']
>>>

'''
