# 5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

# get user's first name and last name and store in variable
name = input('What is your fullname (first name and last name): ')

# split fullname into parts
name_splitted = name.split(' ')

fname = name_splitted[0]
lname = name_splitted[-1]

# print in reverse order with space inbetween
print(lname + ' ' + fname)
