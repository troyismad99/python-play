# for .... else
# also like a nobreak

'''
for item in iterable: 
    if match(item):
        result = item
        break 
else: # nobreak
    # No match found
    result = None 

# Always come here
print(result)
'''

'''
For example, here is a code fragment which ensures that a list of 
integers contains at least one integer divisible by a specified value.

If the supplied list does not contain a multiple of the divisor, 
the divisor itself is appended to the list.
'''
items = [2, 25, 9]
divisor = 12

for item in items:
    if item % divisor == 0:
        found = item
        break 
else: # nobreak
    items.append(divisor)
    found = divisor

print("{items} contains {found} which is a multiple of {divisor}" .format(**locals()))

# The alternative is a function
# 
# Almost any time you see a loop else clause you can 
# refactor it by extracting the loop into a named function

def ensure_has_divisible(items, divisor): 
    for item in items:
        if item % divisor == 0: 
            return item

    items.append(divisor) 
    return divisor

items = [2, 25, 9]
divisor = 12

dividend = ensure_has_divisible(items, divisor)

print("{items} contains {dividend} which is a multiple of {divisor}".format(**locals()))