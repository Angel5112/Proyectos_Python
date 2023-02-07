# Funcion para leer la lista de booleans e imprimir sus elementos linea por linea

def read_booleans(bools_list):
    for element in bools_list:
        print(element)


# Funcion que aplica los string validators para verificar si un elemento del string del string

def validators(word):
    booleans = [False, False, False, False, False]

    for i in range(0, len(word)):
        if word[i].isalnum() == True:
            booleans[0] = True
        if word[i].isalpha() == True:
            booleans[1] = True
        if word[i].isdigit() == True:
            booleans[2] = True
        if word[i].islower() == True:
            booleans[3] = True
        if word[i].isupper() == True:
            booleans[4] = True

    read_booleans(booleans)


if __name__ == '__main__':
    string = input()
    validators(string)