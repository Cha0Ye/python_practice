'''
Write a function called vowel_count that accepts a string and returns a dictionary with the keys as the vowels and values as the count of times that vowel appears in the string.

The function should be case insensitive.

Examples

```py
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

def vowel_count(string):
    '''given a string, return a dictionary of vowel cout with vowel as key, and count as values'''
    vowels = set('aeiou')
    vowels_dictionary = {}
    for letter in string:
        if letter.lower() in vowels:
            vowels_dictionary[letter.lower()] = vowels_dictionary.get(letter.lower(), 0) +1
    
    return vowels_dictionary


