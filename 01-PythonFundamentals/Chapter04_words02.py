from urllib.request import urlopen

# place in function so it is not executed immediatley upon import
def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('UTF-8').split()
            for word in line_words:
                story_words.append(word)

    for word in story_words:
        print(word)

'''
>>> import Chapter04_words02
>>> Chapter04_words02.fetch_words()
It
was
the
'''

# doesn't run at command line

# use __ functions to determine where we are

print(__name__)

'''
repl:
>>> import Chapter04_words02
Chapter04_words02

terminal:
~/D/P/p/01-PythonFundamentals ❯❯❯ python3 Chapter04_words02.py         main ⬆ ◼
__main__

'''

# with this we can run as a script from terminal
if __name__ == '__main__':
    fetch_words()
