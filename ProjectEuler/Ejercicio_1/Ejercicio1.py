"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# Function to find the multiples of 3 or 5 bellow 1000 and sum all of them

def multiples_3_5():
    i = 0
    multiples_sum = 0
    while i < 1000:
        if i % 3 == 0:
            multiples_sum += i
            i += 1
            continue
        elif i % 5 == 0:
            multiples_sum += i
            i += 1
            continue
        else:
            i += 1

    
    return multiples_sum

# Main function

sum = multiples_3_5()
print(f"The sum of all the multiples of 3 or 5 bellow 1000 is: {sum}")