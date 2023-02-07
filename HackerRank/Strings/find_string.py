# Funcion para contar el numero de ocurrencias de un substring

def find_string(string, substring):
    count_str = 0
    sub_length = len(substring)
    str_length = len(string)

    for i in range(0, str_length):
        aux = string[i:i + sub_length]
        if substring in aux:
            count_str += 1

    return count_str

# Entry Point

def run():
    string = input()
    substring = input()
    count = find_string(string, substring)
    print(count)


if __name__ == '__main__':
    run()