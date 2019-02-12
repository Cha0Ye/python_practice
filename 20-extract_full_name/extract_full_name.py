'''
Write a function called extract_full_name. This function should accept a list 
of dictionaries and return a new list of strings with the first and last name 
keys in each dictionary concatenated.
'''

def extract_full_name(lst_name_dict):
    ''' function returns a list of first and last name extracted from an input dictionary'''
    name_list = [f"{name['first']} {name['last']}" for name in lst_name_dict]
    return name_list