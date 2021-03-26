# range is an arithmetic progression of integers

print(range(5))

# stop value is one past the end
for i in range(5):
    print(i)
'''
0
1
2
3
4
'''

# range is "half-open" start is included, but not the end
print(list(range(5,10))) 
# [5, 6, 7, 8, 9]

# step argument
print(list(range(0, 10, 2))) 
# [0, 2, 4, 6, 8]

# prefer enumerate for counters instead of range
# yeids a tuple
t = [6, 372, 8862, 148800, 2096886]
for p in enumerate(t):
    print(p)
'''
(0, 6)
(1, 372)
(2, 8862)
(3, 148800)
(4, 2096886)
'''

# Use tuple unpacking to avoid dealing directly with the tuple
for i, v in enumerate(t):
    print("i = {}, v={}".format(i, v))
'''
i = 0, v=6
i = 1, v=372
i = 2, v=8862
i = 3, v=148800
i = 4, v=2096886
'''

