'''
Write a function called last_element. This function takes in one parameter (a list) and returns the last value in the list. It should return None if the list is empty.

Examples

```py
last_element([1, 2, 3]) # 3
last_element([]) # None
```'''

def last_element(lst):
    '''returns last element in list, returns none if list is empty '''
    if len(lst) == 0:
        return
    return lst[-1]