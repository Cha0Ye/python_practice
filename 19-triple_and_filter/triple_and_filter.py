'''
Write a function called triple_and_filter. This function should accept a list 
of numbers, filter out every number that is not divisible by 4, 
and return a new list where every remaining number is tripled.

Examples

```py
triple_and_filter([1, 2, 3, 4]) # [12]
triple_and_filter([6, 8, 10, 12]) # [24, 36]
```
'''

def triple_and_filter(lst):
    not_div_by_four_nums = [num for num in lst if num % 4 == 0]
    tripled_nums = [num*3 for num in not_div_by_four_nums]
    return tripled_nums