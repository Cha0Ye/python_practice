'''
Write a function called mode. This function accepts a list of numbers and 
returns the most frequent number in the list. You can assume that the mode 
will be unique.

Examples

```py
mode([1, 2, 1]) # 1
mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]) # 4
```
'''
#mode([1,2,1])

def mode(lst):
    '''accepts a list and returns the list item that is most frequent'''
    freq_dict = {}
    max_val_list = []

    for num in lst:
        freq_dict[num] = freq_dict.get(num,0) +1

    for num in freq_dict:
        max_val_list.append(freq_dict[num])

    max_value = max(max_val_list)

    for (key,val) in freq_dict.items():
        if val == max_value:
            return key

        
   



