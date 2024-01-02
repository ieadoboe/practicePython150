'''
7. Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''

# Ask user of filename and store it in a variable
filename = input('What is your filename: ')

# split filename at delimiter (.) into parts
parts = filename.split('.')

# Output extension of the file
print("The extension of the file is: " + repr(parts[-1]))