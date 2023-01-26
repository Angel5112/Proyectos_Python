"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# Funcion para determinar si un numero es divisible desde el 1 al 20

def is_divisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return 0

    return 1


# Funcion para iterar mediante numeros

def numbers():
    i = 0
    while True:
        i += 1
        if is_divisible(i) == 1:
            print(f"El menor numero positivo que es divisible por 1 hasta 20 es: {i}")
            break
        else:
            continue



if __name__ == '__main__':
    numbers()
