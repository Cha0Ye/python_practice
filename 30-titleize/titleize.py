'''Write a function called titleize which accepts a string of words and returns a new string with the first letter of every word in the string capitalized.

Examples

```py
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
```
'''

def titleize(string):
    ''' accepts string; returns string with first letter of each word capitalized'''

    string_list = string.split(' ')

    capitalized_list = [word[0].upper() + word[1:] for word in string_list]

    return (" ").join(capitalized_list)
    

