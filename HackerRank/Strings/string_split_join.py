# Funcion para separar el string y despues volver a unirlo con - en vez de espacios en blanco

def split_and_join(word):
    new_word = word.split(" ")          # split() separa los espacios dados de parametro en una lista de substrings
    joined_word = "-".join(new_word)    # join() une dichos espacios dados en un string denuevo pero reemplazando
                                        # espacios con el substring dado antes del metodo
    return joined_word


# Entry point

def run():
    line = input()
    result = split_and_join(line)
    print(result)


if __name__ == '__main__':
    run()