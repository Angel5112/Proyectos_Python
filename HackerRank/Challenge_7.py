"""
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:

123...n

Note that "..." represents the consecutive values in between.

Example

n = 5

Print the string 12345.

Input Format

The first line contains an integer n.

Constraints

1 <= n <= 150
"""

#STDIN

n = int(input())
solution = ''

# Solucion

for i in range(1, n):
    character = str(i)
    solution += character

print(solution + str(n))