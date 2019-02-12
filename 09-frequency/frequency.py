'''
Write a function called frequency. This function accepts a list and a search term (this will always be a primitive value) 
and returns the number of times the search term appears in the list.

Examples

```py
frequency([1, 2, 3, 4, 4, 4], 4) # 3
frequency([True, False, True, True], False) # 1
```
'''

def frequency(lst, val):
    '''accepts a list and a search term, return the number of times the search term appears'''
    
    return lst.count(val) 
