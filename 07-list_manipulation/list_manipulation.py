'''
Write a function called list_manipulation. This function should take in three parameters (a list, command, and location), 
along with an optional fourth parameter (a value).
Examples

```py
l = [1, 2, 3]
list_manipulation(l, "remove", "end" # 3)
l # [1, 2]
list_manipulation(l, "remove", "beginning") # 1
l # [2]
list_manipulation(l, "add", "beginning", 20) # [20, 2]
list_manipulation(l, "add", "end", 30) # [20, 2, 30]
If the command is "remove" and the location is "end", the function should remove the last value in the 
list and return the value removed.
If the command is "remove" and the location is "beginning", the function should remove 
the first value in the list and return the value removed.
If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) 
to the beginning of the list and return the list.
If the command is "add" and the location is "end", the function should add the value (fourth parameter) 
to the end of the list and return the list.

```
'''

def list_manipulation(lst, cmd, location, val = None):
    cmd = cmd.lower()
    location = location.lower()
    if cmd == 'remove' and location == 'end':
        return lst.pop()
    elif cmd =='remove' and location == 'beginning':
        return lst.pop(0)
    elif cmd == 'add' and location == 'beginning':
        lst.insert(0, val)
        return lst
    elif cmd == 'add' and location =='end':
        lst.append(val)
        return lst
