import random

# Funcion para obtener un numero random dado un intervalo definido por el usuario

rand_num = lambda a, b: random.randint(a, b)

# Funcion para jugar al juego

def guess_num(num, a, b):
    while True:
        user_num = int(input(f"Ingrese un numero del {a} al {b}: "))
        if user_num == num:
            print(f"Correcto! El numero es {num}!\n")
            break
        elif user_num > num:
            print("El numero se encuentra mas a la izquierda!\n")
        else:
            print("El numero esta mas a la derecha!\n")
    
