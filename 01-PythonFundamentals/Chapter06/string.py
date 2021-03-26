#str is a homogeneous immutable sequence of Unicode codepoints (characters)

# Welsh place Llanfair PG for short
print(len("Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"))
# 58

# concatenation
print("New" + "found" + "land")
# Newfoundland

# strings are immutable so the += rebinds to a new object
s = "New"
s += "found"
s += "land"
print(s)

# use sparingly concatenation with + or += can cause performance degradation
# can generate large numbers of temporary strings, memory allocations, and copies

# using join
print( ''.join(["New", "found", "land"]))
# Newfoundland

# call join on the concat operator, in this the empty string

# partition -> divide the string into three parts
# a tuple with three elements before separator, separator, and after separator

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x) 
#('I could eat ', 'bananas', ' all day')

y = txt.partition("apples")
print(y) 
#('I could eat bananas all day', '', '')

