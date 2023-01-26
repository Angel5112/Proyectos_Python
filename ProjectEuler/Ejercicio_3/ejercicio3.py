"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Function to find if a number is prime (returns 1) or not (returns 0)

def is_prime(p):

    i = 2
    n = p // 2
    while i <= n:
        if p % i == 0:
            return 0
        i += 1
    
    return 1


# Function to find the largest prime factor of a number

def largest_prime_factor(n):

    i = 1
    largest_prime = n
    while i <= n // 2:
        i += 1
        if n % i == 0:
            if is_prime(i) == 1:
                largest_prime = i
                continue
            else:
                continue

    return largest_prime


# Main function

num = 600851475143
large_prime = largest_prime_factor(num)
print(f"\nThe largest prime factor of {num} is: {large_prime}\n")
