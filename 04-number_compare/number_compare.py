'''Write a function called number_compare. This function takes in two parameters (both numbers). If the first is greater than the second, this function returns "First is greater." If the second number is greater than the first, the function returns "Second is greater." Otherwise the function returns "Numbers are equal."

Examples

```py
number_compare(1, 1) # "Numbers are equal"
number_compare(1, 0) # "First is greater"
number_compare(2, 4) # "Second is greater"
```'''

def number_compare(num1, num2):
    '''accepts 2 numbers; if first number is greater than second, return "First is greater"; 
    if second is greater, return "Second is greater."; else return "Numbers are equal."'''

    if num1 > num2:
        return "First is greater"
    elif num2 > num1:
        return "Second is greater"
    else:
        return "Numbers are equal"