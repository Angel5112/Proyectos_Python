# Funcion para cambiar minusculas a mayusculas y viceversa

def swap_case(word):
    new_word = ''
    for letter in word:
        new_word = new_word + letter.swapcase()     # Los metodos de string no cambian el original, retorna un valor
                                                    # swapcase() cambia minuscula a mayuscula y viceversa
    return new_word


if __name__ == '__main__':
    string = input()
    word = swap_case(string)
    print(word)