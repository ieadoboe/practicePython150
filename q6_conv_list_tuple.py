'''
6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

# ask user for comma separated values and store in variable
user_csv = input('enter your values: ')

# split values into list and convert to tuple
list = user_csv.split(", ")
tuple = tuple(list)

# output list of csv
print('list: ', list)

# output tuple of csv
print('tuple: ', tuple)
