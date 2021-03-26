# words.py sample

Using type and dir to examine modules and functions

``` terminal
~/D/P/p/01-PythonFundamentals ❯❯❯ cd Chapter05                                        main
~/D/P/p/0/Chapter05 ❯❯❯ python3                                                   main ⬆ ◼
Python 3.9.2 (default, Mar 15 2021, 10:13:36) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import words
>>> type(words)
<class 'module'>
>>> dir(words)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fetch_words', 'main', 'print_items', 'sys', 'urlopen']
>>> type(words.fetch_words)
<class 'function'>
>>> dir(words.fetch_words)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


>>> words.fetch_words.__name__
'fetch_words'
>>> words.fetch_words.__doc__
'Fetch a list of words from a URL.\n    \n    Args:\n        url: The URL of a UTF-8 text document.\n    \n    Returns:\n        A list of strings containing the words from\n        the document.\n    \n    '


```
