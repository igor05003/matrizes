import sys
import os
import lerMatriz

A = lerMatriz.Ler("matriz_A.txt")


print("A")

i = 0
j = 0
while(i < 4):
    if j < 4:
        print(f'{A[i][j]}\t', end = "")
        j = j + 1
    else:
        print("")
        i = i + 1
        j = 0
