import sys
import os
import string
import lerMatriz

A = lerMatriz.Ler("matriz_A.txt")


print("A triangular inferior")

i = 0
j = 0
while(i < 4):
    if j == i:
        print(f'{A[i][j]}\t', end = "")
        i = i + 1
        j = 0
        print("")
    else:
        print(f'{A[i][j]}\t', end = "")
        j = j + 1
