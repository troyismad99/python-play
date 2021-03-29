# Two constructs:
    
# Iterable Protocol
    # Iterable objects can be passed to the iter() function
    # to get an iterable.

# Iterator Protocol
    # Iterator objects can be passed to the next() function 
    # to fetch the next item.

a = ['Spring', 'Summer', 'Autumn', 'Winter']

i = iter(a)

print(next(i)) # Spring
print(next(i)) # Summer
print(next(i)) # Autumn
print(next(i)) # Winter

# print(next(i)) # Exception StopIteration


