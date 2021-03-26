from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('UTF-8').split()
        for word in line_words:
            story_words.append(word)

# run from command line
'''
~/D/P/python-play ❯❯❯ cd 01-PythonFundamentals                         main ⬆ ◼
~/D/P/p/01-PythonFundamentals ❯❯❯ l                                    main ⬆ ◼
total 48
drwxr-xr-x   7 troy  staff   224 26 Mar 10:03 .
drwxr-xr-x  11 troy  staff   352 25 Mar 15:40 ..
-rw-r--r--   1 troy  staff  6803 23 Mar 14:54 Chapter02a.txt
-rw-r--r--   1 troy  staff   890 24 Mar 10:29 Chapter02b.txt
-rw-r--r--   1 troy  staff  3921 26 Mar 09:55 Chapter03.py
-rw-r--r--   1 troy  staff   257 26 Mar 10:03 Chapter04_words.py
-rw-r--r--   1 troy  staff   376 23 Mar 13:11 Pluralsight.md
~/D/P/p/01-PythonFundamentals ❯❯❯ python3 Chapter04_words.py           main ⬆ ◼
~/D/P/p/01-PythonFundamentals ❯❯❯                                      main ⬆ ◼
'''
# nothing happens, add loop to print words

for word in story_words:
    print(word)

# now we get all the words
'''
~/D/P/p/01-PythonFundamentals ❯❯❯ python3 Chapter04_words.py           main ⬆ ◼
It
was
the
best
of
times
it
was
the
worst
of
times
it
was
the
age
of
wisdom
it
was
the
age
of
foolishness
it
was
the
epoch
of
belief
it
was
the
epoch
of
incredulity
it
was
the
season
of
Light
it
was
the
season
of
Darkness
it
was
the
spring
of
hope
it
was
the
winter
of
despair
we
had
everything
before
us
we
had
nothing
before
us
we
were
all
going
direct
to
Heaven
we
were
all
going
direct
the
other
way
in
short
the
period
was
so
far
like
the
present
period
that
some
of
its
noisiest
authorities
insisted
on
its
being
received
for
good
or
for
evil
in
the
superlative
degree
of
comparison
only
'''
