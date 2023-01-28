# List Comprehension: Find all permutations of i, j, k that the sum does not exceed n and add all possiblities in a new list

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    new_list = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if i + j + k != n]

    print(new_list)