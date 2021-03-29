# Look before you leap (LBYL)
#        vs
# It's easier to ask forgiveness than permission (EAFP)

# Python strongly favours EAFP -> 
# Do the happy path rather than intersperse a bunch of error logic
# handle the exceptions separately

import os

def process_file(p):
    # some fancy code here
    pass

# LBYL version:
def LBYL():
    p = '/path/to/datafile.dat'

    if os.path.exists(p): 
        process_file(p)
    else:
        print('No such file as {}'.format(p))

    # only an exitence check, what if it contains garbage? What if it's a directory?
    # Race condition? It could be deleted between existence check and the process. 
    #                 A classic atomicity issue

    # Error codes require interspersed, local handling.
    # Error codes are silent by default.



def EAFP():
    p = '/path/to/datafile.dat'

    try:
        process_file(p)
    except OSError as e:
        print('Could not process file because{}'.format(str(e)))


# Exceptions allow centralized, non-local handling.
# Exceptions require explicit handling and connot be easily ignored
