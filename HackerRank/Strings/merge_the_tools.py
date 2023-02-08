# Funcion para hallar las posibles combinaciones de substrings

def merge_the_tools(string, k):
    length = len(string)
    for i in range(0, length, k):
        combination = []
        aux_string = []
        aux_string.extend(string[i:i+k])

        for j in range(0, len(aux_string)):
            if aux_string[j] in combination:
                continue
            else:
                combination.append(aux_string[j])

        combination = ''.join(combination)
        print(combination)


if __name__ == '__main__':
    string = input()
    length = int(input())
    merge_the_tools(string, length)