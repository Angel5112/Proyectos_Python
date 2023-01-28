"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]

The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that score: ["beta", "alpha"]. Ordered alphabetically, the names are printed as: alpha
beta

Constraints:

2 <= N <= 5

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
"""

if __name__ == '__main__':
    class_name_marks = []       # Creando lista 2D de Nombres y Notas
    marks = []                  # Creando Lista 1D de Notas
    for n in range(int(input())):
        name = input()
        score = float(input())
        class_name_marks.append([name, score])  # Rellenando lista 2D
        marks.append(score)                     # Rellenando lista 1D

    marks = sorted(set(marks))      # Hacemos un set (eliminamos repetidos) y ordenamos de menor a mayor (volviendo a lista)
    second_lowest_grade = marks[1]  # El segundo elemento siempre sera la segunda nota mas baja

    # Creamos lista de nombres que coincidan con la nota mas baja
    
    names_second_lowest_grade = [class_name_marks[name][0] for name in range(0, len(class_name_marks)) if class_name_marks[name][1] == second_lowest_grade] 
    
    names_second_lowest_grade.sort()    # Ordenamos los nombres alfabeticamente

    # Recorremos la lista de nombres con la segunda nota mas baja para imprimirlos uno a uno

    for i in range(0, len(names_second_lowest_grade)):
        print(names_second_lowest_grade[i])
    
