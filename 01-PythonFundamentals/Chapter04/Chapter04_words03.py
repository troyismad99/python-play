#!/usr/bin/env python3
""" Retrieve and print words from a URL.

Usage:

    python3 Chapter04_words03.py <URL>
"""
import sys
from urllib.request import urlopen

# 'http://sixty-north.com/c/t.txt'
def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
    
    Returns:
        A list of strings containing the words from
        the document.
    
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('UTF-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the filename

'''
>>> from Chapter04_words03 import (fetch_words, print_words)
>>> print_words(fetch_words())
It
was
the

# import everything NOTE: Only for casual use in the repl, bad practice
>>> from Chapter04_words03 import *

print_words prints anything, rename to print_items

'''

# added docstring with the triple """
# above follows the google pythin style guide

'''
~/D/P/p/01-PythonFundamentals ❯❯❯ python3                              main ⬆ ◼
Python 3.9.2 (default, Mar 15 2021, 10:13:36) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from Chapter04_words03 import (fetch_words, print_items)
>>> help(fetch_words)
Help on function fetch_words in module Chapter04_words03:

fetch_words(url)
    Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
    
    Returns:
        A list of strings containing the words from
        the document.

'''

'''
~/D/P/p/01-PythonFundamentals ❯❯❯ python3                              main ⬆ ◼
Python 3.9.2 (default, Mar 15 2021, 10:13:36) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import Chapter04_words03
>>> help(Chapter04_words03)
Help on module Chapter04_words03:

NAME
    Chapter04_words03 - Retrieve and print words from a URL.

DESCRIPTION
    Usage:
    
        python3 Chapter04_words03.py <URL>

FUNCTIONS
    fetch_words(url)
        Fetch a list of words from a URL.
        
        Args:
            url: The URL of a UTF-8 text document.
        
        Returns:
            A list of strings containing the words from
            the document.
    
    main(url)
        Print each word from a text document from a URL.
        
        Args:
            url: The URL of a UTF-8 text document.
    
    print_items(items)
        Print items one per line.
        
        Args:
            An iterable series of printable items.

FILE
    /Users/troy/Development/Python/python-play/01-PythonFundamentals/Chapter04_w

'''


# The Whole Shebang
# first line of file add for python : #!/usr/bin/env python3
# can now run the script directly
'''
~/D/P/p/01-PythonFundamentals ❯❯❯ chmod +x Chapter04_words03.py                   main ⬆ ◼
~/D/P/p/01-PythonFundamentals ❯❯❯ ./Chapter04_words03.py http://sixty-north.com/c/t.txt
It
was


'''