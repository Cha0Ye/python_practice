'''
Write a function called flip_case. This function accepts a string and a letter and 
reverses the case of all occurrences of the letter in the string.

Examples

```py
flip_case("Hardy har har", "h") # "hardy Har Har"
flip_case("Aaaaahhh!", "A") # "aAAAAhhh!"
```
'''

def flip_case(str,char):
    flipped_str = ''

    for letter in str:
        if letter == char.upper():
            flipped_str += letter.lower()
        elif letter == char.lower():
            flipped_str += letter.upper()
        else:
            flipped_str += letter
    return flipped_str
