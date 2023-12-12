Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> txt = "Hello World!"
>>> print(txt[0:2])
He
>>> print(txt[3])
l
>>> print(txt[::2])
HloWrd
>>> print(txt[1::2])
el ol!
>>> 
>>> 
>>> 
>>> fruits = ['apple','pear','kiwi']
>>> print(fruits[1:])
['pear', 'kiwi']
>>> ['pear', 'kiwi']
['pear', 'kiwi']
>>> 
>>> fruits[0:0] = 'strawberry'
>>> print(fruits)
['s', 't', 'r', 'a', 'w', 'b', 'e', 'r', 'r', 'y', 'apple', 'pear', 'kiwi']
>>> 
>>> 
>>> fruits[0] = 'strawberry'
>>> print(fruits)
['strawberry', 't', 'r', 'a', 'w', 'b', 'e', 'r', 'r', 'y', 'apple', 'pear', 'kiwi']
