# try ... except ... else
'''
In this case, the else clause is executed if no exception is raised:

try:
    # This code might raise an exception 
    # do_something()
except ValueError:
    # ValueError caught and handled 
    handle_value_error()
else:
    # No exception was raised
    # We know that do_something() succeeded, so 
    do_something_else()

# Looking at this, you might wonder why we don’t call do_something_else() 
# on the line after do_something(), like this:

try:
    # This code might raise an exception 
    do_something()
    do_something_else()
except ValueError:
    # ValueError caught and handled 
    handle_value_error()

# The downside of this approach, is that we now have no way of telling 
# in the except block whether it was do_something() or do_something_else() 
# which raised the exception. 
# The enlarged scope of the try block also obscures our intent with 
# catching the exception; where are we expecting the exception to come from?

'''

filename = ""

try:
    f = open(filename, 'r')
except OSError: 
    # OSError replaces IOError from Python 3.3 onwards 
    print("File could not be opened for read")
else:
    # Now we're sure the file is open 
    print("Number of lines", sum(1 for line in f)) 
    f.close()

