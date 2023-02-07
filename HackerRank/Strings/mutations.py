# Funcion para hacer la mutacion al string

def mutation(word, pos, letter):
    word = list(word)
    word[int(pos)] = letter
    word = ''.join(word)
    return word


# Entry Point

def run():
    string = input()
    position, value = input().split()
    new_string = mutation(string, position, value)
    print(new_string)


if __name__ == '__main__':
    run()