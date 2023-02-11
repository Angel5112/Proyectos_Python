# Proyecto de adivinar un numero aleatorio (dado el intervalo) y dependiendo de la respuesta del usuario, se imprime si esta a la izquierda o a la derecha

from pkg import numbers

# Entry point

def run():
    x = int(input("Ingresa el menor numero del intervalo: "))
    y = int(input("Ingresa el mayor numero del intervalo: "))
    num = numbers.rand_num(x, y)
    numbers.guess_num(num, x, y)

if __name__ == '__main__':
    run()