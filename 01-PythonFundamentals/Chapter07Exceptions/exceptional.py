def convert(s):
    '''Convert to integer.'''
    x = int(s)
    return x

print(convert("33")) # 33

#print(convert("abcde"))
'''
Traceback (most recent call last):
  File "exceptional.py", line 8, in <module>
    convert("abcde")
  File "exceptional.py", line 3, in convert
    x = int(s)
ValueError: invalid literal for int() with base 10: 'abcde'
'''

def convert2(s):
    '''Convert to integer.'''
    try:
        x = int(s)
        print("Conversion succeeded. x =", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    return x

print(convert2("33")) # 33
print(convert2("abcde"))
'''
Conversion succeeded. x = 33
33
Conversion failed!
-1
'''

# try a list with the int ctor
#print(convert2([4, 5, 7]))
'''
Traceback (most recent call last):
  File "exceptional.py", line 38, in <module>
    print(convert2([4, 5, 7]))
  File "exceptional.py", line 21, in convert2
    x = int(s)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
'''

def convert3(s):
    '''Convert to integer.'''
    try:
        x = int(s)
        print("Conversion succeeded. x =", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    except TypeError:
        print("Conversion failed!")
        x = -1
    return x

print(convert3([4, 5, 7])) # Conversion failed! -1

# clean up duplicate code

def convert4(s):
    '''Convert to integer.'''
    x = -1
    try:
        x = int(s)
        print("Conversion succeeded. x =", x)
    except ( ValueError, TypeError):
        print("Conversion failed!")
    return x

# remove the prints, but then indent error needs a noop
def convert5(s):
    '''Convert to integer.'''
    x = -1
    try:
        x = int(s)
    except ( ValueError, TypeError):
        pass # empty block
    return x

import sys

def convert6(s):
    '''Convert to integer.'''
    try:
        return int(s)
    except ( ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        return -1

print(convert6([4, 5, 7])) # Conversion error: int() argument must be a string, a bytes-like object or a number, not 'list'

import math

def string_log(s):
    v = convert6(s)
    return math.log(v)




def convert7(s):
    '''Convert to integer.'''
    try:
        return int(s)
    except ( ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        raise # re-raise the exception up





