import sys
import os
import string
import lerMatriz

A = lerMatriz.Ler("matriz_A.txt")
B = lerMatriz.Ler("matriz_B.txt")

C = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("A + B = C")
j = 0
i = 0
while(i < 4):
    if j < 4:
        C[i][j] = A[i][j] + B[i][j]
        print(f'{C[i][j]}\t', end = "")
        j = j + 1
    else:
        print("")
        i = i + 1
        j = 0
