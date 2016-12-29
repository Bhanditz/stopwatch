# Stopwatch
Simple Python module to keep track of multiple concurrent timers.

## Installation
- Dependencies: Python 3
- Build Dependencies: git (only for Arch Linux python-stopwatch-git package)

### Universal
```
$ python setup.py sdist
# python setup.py
```
### Arch Linux
Run this in an empty directory.
```sh
$ wget https://raw.githubusercontent.com/dnut/PKGBUILDs/master/stopwatch/python-stopwatch-git/PKGBUILD
$ makepkg -si
```

## Usage
```python
from stopwatch import Stopwatch

t = Stopwatch()
t.start('Optionally select a label')
"""
some procedure here
"""
t.start('Optionally select annother label')
# Now two timers are timing at once.
t.stop('which timer label to stop, else most recent')
t.end()
```
Most of the methods that print output can be quieted by setting the optional paramater ```quiet=True```. See source code for more complete documentation.

Python shell example:
```python
>>> from stopwatch import Stopwatch
>>> t = Stopwatch()
>>> t.start()
>>> t.stop()
Procedure #1: 3.1 s
>>> t.start()
>>> t.start('hello')
>>> t.stop('Procedure #2')
Procedure #2: 20 s
>>> t.lap()
hello: 17 s
>>> t.lap('next one')
Procedure #3: 6.9 s
>>> t.lap('another next one', quiet=True)
>>> t.end()

Done.

== Times ==
Total: 55 s
Procedure #1: 3.1 s
Procedure #2: 20 s
hello: 17 s
Procedure #3: 6.9 s
next one: 11 s
another next one: 4 s
```
