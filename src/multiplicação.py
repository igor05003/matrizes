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

print("A * B = C")
print(len(A[0]))
print(len(B))
if (len(A[0])) != (len(B)):
    print("Erro! Esta multiplicação não pode ser calculada")
else:
    i = 0
    while(i < 4):
        j = 0
        while(j < 4):
            summ = 0
            k = 0
            while(k < 4):
                summ = summ + A[i][k] * B[k][j]
                k = k + 1
            C[i][j] = summ
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
