'''
Write a function called compact. This function accepts a list and returns a list of values that are truthy values.

Example

```py
compact([0, 1, 2, "", [], False, {}, None, "All done"])
# [1, 2, "All done"]
```
'''


def compact(lst):
    ''' returns lst with only truthy values'''
    return [val for val in lst if bool(val) == True]