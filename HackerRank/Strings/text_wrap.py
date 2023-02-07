import textwrap

def wrap(string, max_width):
    new_string = textwrap.wrap(string, max_width)       # wrap() crea una lista con elementos de width caracteres pertenecientes al string original
    new_string = '\n'.join(new_string)
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)