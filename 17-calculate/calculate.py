'''
- `operation`, a string which must be 'add', 'subtract', 'multiply', or 'divide'.

- `first`, which is a number

- `second`, which is another number

- `make_int`, a boolean (this should default to False)

- `message` which is a string (which can be omitted).
'''


def calculate(operation, first, second, make_int = False, message=''):
    return_message = "The result is"
    if operation == 'add':
        if make_int == True:
            return f"{return_message} {int(first+second)}"
        else:
           return f"{return_message} {first+second}" 