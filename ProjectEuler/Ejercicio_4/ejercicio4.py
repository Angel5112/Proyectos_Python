"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Funcion para determinar si un numero es palindrome\

def is_palindrome(product):
    count = iteration_count = 0
    aux = str(product)
    size = len(aux)
    if (size % 2 == 0):
        palindrome = size // 2
    else:
        palindrome = (size // 2) + 1

    for i in aux:
        iteration_count += 1
        if i == aux[-iteration_count]:
            count += 1
        if iteration_count == palindrome:
            break
    
    if count == palindrome:
        return 1
    else:
        return 0

# Funcion para hallar el mayor palindrome del producto de dos numeros de 3 digitos

def products(x, y):

    max_palindrome = (999 * 999) * (-1)
    for i in range(x, 1000):
        for j in range(y, 1000):
            product = i * j
            if is_palindrome(product) == 1:
                if product > max_palindrome:
                    max_palindrome = product

    return max_palindrome


if __name__ == '__main__':
    a = b = 100
    m_palindrome = products(a, b)
    print(f"El mayor palindrome del producto de numeros de 3 digitos es: {m_palindrome}")