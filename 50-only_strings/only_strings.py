'''
Write a function called only_strings.

This function should return True if the value of every argument is a string.

Otherwise, it should return False.

Hint: go learn about the function `all()`; it will help here!

Examples

```py
only_strings("hello", "world") # True
only_strings(1, "bye") # False
only_strings(string1="string", string2="other string") # True
only_strings([], string="yep") # False
only_strings("so", "many", wait_for_it="strings") # True
only_strings() # True
```
'''

def only_strings(*args):
    '''returns true if all arguments are of type string, otherwise return false'''
    for arg in args:
        if(type(arg) != str):
            return False
    
    return True