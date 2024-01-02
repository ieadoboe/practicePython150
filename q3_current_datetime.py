# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14


# importing date module
from datetime import datetime

# storing current date in variable
current_dt = datetime.now()

# Displays current date and time
print('Current date and time:\n', current_dt.strftime('%a %d-%m-%Y, %H:%M:%S'))
