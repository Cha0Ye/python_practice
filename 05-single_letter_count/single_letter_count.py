'''
Write a function called single_letter_count. This function takes in two parameters (two strings). 
The first parameter should be a word and the second should be a letter. 
The function returns the number of times that letter appears in the word. 
The function should be case insensitive (does not matter if the input is lowercase or uppercase). 
If the letter is not found in the word, the function should return 0.

Examples

```py
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
```
'''

def single_letter_count(str1, char):
    '''function takes in char and string, returns how many times char appears in string. if not found, return 0 '''
    lower_case_str = str1.lower()
    lower_case_char = char.lower()
    return lower_case_str.count(lower_case_char)