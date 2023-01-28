"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints: 2 <= n <= 10 and -100 <= A[i] <= 100
"""

# Creacion de la lista de scores

if __name__ == '__main__':
    n = int(input())

    # Esta parte de abajo no sirve por que el usuario inserta '2 3 6 6 5' de una y input.split separa cada elemento
    # en una lista, lo mio hace una lista de una pero al recibir esa entrada completa, no funciona
    # score_list = [int(input()) for i in range(0, n)]

    # Lo ideal es lo siguiente

    score_list = map(int, input().split())
    
    # Transformamos la lista a set y lo ordenamos, pero sorted() transformara el set a una lista denuevo

    score_list = sorted(set(score_list))

    # Como la lista ya esta ordenada con sorted[] y no hay elementos repetidos (por set() ), el penultimo elemento
    # sera el segundo mayor
    
    print(score_list[-2])
