'''
 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''

# Ask user for integer and save in variable n
n = int(input('Provide integer: '))

# Compute n + nn + nnn
n1 = int("%i" % n)
n2 = int("%i%i" % (n, n))
n3 = int("%i%i%i" % (n, n, n))

print(n1 + n2 + n3)
