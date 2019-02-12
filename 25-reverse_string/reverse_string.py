'''
Write a function called reverse_string which accepts a string and returns a new string with all the characters reversed.

Examples

```py
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
```
'''

def reverse_string(some_str):
    '''returns an input string in reverse order'''
    return some_str[-1::-1]
