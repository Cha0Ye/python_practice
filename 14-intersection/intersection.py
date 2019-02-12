'''Write a function called intersection. This function should accept two lists and 
return a list with the values that are in both input lists.

Example

```py
intersection([1, 2, 3], [2, 3, 4]) # [2, 3]
'''

def intersection(lst1, lst2):
    ''' return a list containing numbers in list one and list two'''

    set1 = set(lst1)
    set2 = set(lst2)

    return list(set1 & set2)