
m = [9, 15, 24]

def modify(k):
    k.append(39)
    print("k=", k)

modify(m)
print(m) # we have changed the list that both m and k reference

f =[14, 23, 37]
def replace(g):
    g = [17, 28, 45] # reassign the reference g to point to a new list
    print("g=", g)

replace(f)
print(f) # we changed g to reference a different list

# default value
def banner(message, border = '-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner('hello')
banner("Sun, moon and stars", "*")
banner("Sun, moon and stars", border="*")
