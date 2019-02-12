'''
- `operation`, a string which must be 'add', 'subtract', 'multiply', or 'divide'.

- `first`, which is a number

- `second`, which is another number

- `make_int`, a boolean (this should default to False)

- `message` which is a string (which can be omitted).
'''


def calculate(operation, first, second, make_int = False, message=None):
    operation_result = 0
    return_message = ''
    if message == None:
        return_message = "The result is"
    elif message != None:
        return_message = message

    if operation == 'add':
        operation_result = first + second
    elif operation == 'subtract':
        operation_result = second - first
    elif operation == 'multiply':
        operation_result = first*second
    elif operation == 'divide':
        operation_result = first/second

    if make_int == False:
        return f"{return_message} {operation_result}"
    elif make_int == True:
        return f"{return_message} {int(operation_result)}"


