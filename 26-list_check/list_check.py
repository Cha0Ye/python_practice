'''
Write a function called `all_lists`, which accepts a list and returns True
 if each value in the list is a list. Otherwise the function should return False.

You can discover if an thing is a list with "isinstance(item, list)".

Examples

```py
all_lists([[], [1], [2, 3], (1, 2)]) # False
all_lists([1, True, [], [1], [2, 3]]) # False
all_lists([[], [1], [2, 3]]) # True
```
'''

def all_lists(input_lst):
    '''returns true if every item in the input list is a list'''
    for item in input_lst:
        if not isinstance(item, list):
            return False
    return True


print(all_lists([[], [1], [2, 3], (1, 2)])) # False
print(all_lists([1, True, [], [1], [2, 3]])) # False
print(all_lists([[], [1], [2, 3]])) # True