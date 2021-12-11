'''
Stolen from: https://realpython.com/python-f-strings/
'''

print('Option one is percent formatting:')
# Only ints, strs, and doubles can be formatted

name = 'Troy'
print('Hello %s.' % name )

# tuple for more than one value.
day = 'Sunday'
print('Hello %s. Today is %s.' % (name, day) )

# hard to read with longer strings
temperature = 80
city = 'Chemainus'
weather = 'sunny'
print('Hello %s. It is currently a %s %s and %s degrees in %s today.' % (name,  weather, day,temperature, city) )

print('*************************')
print('Option two: str.format')

print('Hello {}.'.format(name))
print('Hello {}. Today is {}.'.format(name, day))

# can use an index, and reference in any order
print('Hello {0}. Today is {1}.'.format(name, day))
print('Hello {1}. Today is {0}.'.format(day, name))

# variable names allow us to use objects like dictionaries
d = {'name': 'Troy', 'today': 'Sunday'}
print('Hello {name}. Today is {today}.'.format(name=d['name'], today=d['today']))

# shortcut with unpacking
print('Hello {name}! Today is {today}.'.format(**d))

# can still be very verbose
print('Hello {name}. It is currently a {weather} {day} and {temperature} degrees in {city} today.'.format(name=name, weather=weather, day=day, temperature=temperature, city=city))

print('*************************')
print('Option three: f-Strings')
# aka formatted string literals
# Python 3.6 -> PEP 498 https://www.python.org/dev/peps/pep-0498/

print(f'Hello {name}.')
print(f'Hello {name}. Today is {day}.')

# can call methods
print(f'Hello {name.lower()}. Today is {day.upper()}.')

class Person:
    def __init__(self, first_name : str, last_name: str, wg: int):
        self.first_name = first_name
        self.last_name = last_name
        self.wg = wg

    def __str__(self):
        return f"{self.first_name} {self.last_name} wg number {self.wg}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} wg number {self.wg}. Surprise!"

'''
The __str__() and __repr__() methods deal with how objects are presented as strings, 
so you’ll need to make sure you include at least one of those methods in your class definition. 

If you have to pick one, go with __repr__() because it can be used in place of __str__().

The string returned by __str__() is the informal string representation of an object and should be readable. 

The string returned by __repr__() is the official representation and should be unambiguous. 

Calling str() and repr() is preferable to using __str__() and __repr__() directly.

By default, f-strings will use __str__(), but you can make sure they use __repr__() if you include the conversion flag !r:
'''

me = Person("Troy", "Hamilton", 99 )

print(f"{me}")
print(f"{me!r}")

print(f'Hello {name}. It is currently a {weather} {day} and {temperature} degrees in {city} today.')

