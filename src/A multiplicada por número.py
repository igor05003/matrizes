import sys
import os
import string
import lerMatriz

A = lerMatriz.Ler("matriz_A.txt")

C = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]



print("a*A = C")
a = float(input("a = " ))

i = 0
while(i < 4):
    j = 0
    while(j < 4):
        C[i][j] = A[i][j] * a
        j = j + 1

    i = i + 1

i = 0
while(i < 4):
    j = 0
    while(j < 4):
        print(f'{C[i][j]}\t', end = "")
        j = j + 1

    print("")
    i = i + 1
