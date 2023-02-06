'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i .
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''

# Funcion para leer la operacion y realizarla en la lista

def operations(n, new_list):
    op, *element = input().split()
    element = [int(x) for x in element]
    if op == 'insert':
        new_list.insert(element[0], element[1])
    elif op == 'print':
        print(new_list)
    elif op == 'remove':
        new_list.remove(element[0])
    elif op == 'append':
        new_list.append(element[0])
    elif op == 'sort':
        new_list.sort()
    elif op == 'pop':
        new_list.pop()
    elif op == 'reverse':
        new_list.reverse()
    
    return new_list

# Entry point

def run():
    N = int(input())    # Cantidad de operaciones
    new_list = []
    for i in range(0, N):
        new_list = operations(N, new_list)


if __name__ == '__main__':
    run()