'''
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''

# Ask for python function and store in variable
py_func_name = input('What function do you want to be described: ')

# Find built in docstring from source code
try :
    py_func = getattr(__builtins__, py_func_name[:-2])
    print(py_func.__doc__)
except :
    print(f'Function {py_func_name} not found.')