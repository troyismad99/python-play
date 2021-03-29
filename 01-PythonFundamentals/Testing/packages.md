# Packages

Install into a virtual environment with pip.

``` terminal
~/D/P/p/0/Testing ❯❯❯ python3 -m venv test_env                                                                         main ◼
~/D/P/p/0/Testing ❯❯❯ python3 -m venv .venv                                                                            main ◼
~/D/P/p/0/Testing ❯❯❯ source .venv/bin/activate                                                                        main ◼
(.venv) ~/D/P/p/0/Testing ❯❯❯                                                                                          main ◼
(.venv) ~/D/P/p/0/Testing ❯❯❯ pip intall --upgrade pip                                                                 main ◼
ERROR: unknown command "intall" - maybe you meant "install"
(.venv) ~/D/P/p/0/Testing ❯❯❯ pip install --upgrade pip                                                            ✘ 1 main ◼
Requirement already satisfied: pip in ./.venv/lib/python3.9/site-packages (21.0.1)
(.venv) ~/D/P/p/0/Testing ❯❯❯                                                                                          main ◼
(.venv) ~/D/P/p/0/Testing ❯❯❯ pip install nose                                                                         main ◼
Collecting nose
  Downloading nose-1.3.7-py3-none-any.whl (154 kB)
     |████████████████████████████████| 154 kB 3.1 MB/s 
Installing collected packages: nose
Successfully installed nose-1.3.7
(.venv) ~/D/P/p/0/Testing ❯❯❯ python3                                                                                  main ◼
Python 3.9.2 (default, Mar 15 2021, 10:13:36) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import nose
>>> nose.__file__
'/Users/troy/Development/Python/python-play/01-PythonFundamentals/Testing/.venv/lib/python3.9/site-packages/nose/__init__.py'
>>> 
(.venv) ~/D/P/p/0/Testing ❯❯❯ nosetests palindrome.py                                                                  main ◼
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
(.venv) ~/D/P/p/0/Testing ❯❯❯ deactivate                                                                               main ◼
~/D/P/p/0/Testing ❯❯❯                                                                                                  main ◼
```
