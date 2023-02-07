# Funcion para unir first_name y last_name en una oracion

def join(first, last):
    message = f"Hello {first} {last}! You just delved into python."
    print(message)


# Entry point

def run():
    first_name = input()
    last_name = input()
    join(first_name, last_name)


if __name__ == '__main__':
    run()