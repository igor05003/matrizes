import sys
import os
import string
import lerMatriz
import multiplicador
import imprimir

A = lerMatriz.Ler("matriz_A.txt")
B = lerMatriz.Ler("matriz_B.txt")


print("A * B = C")
C = multiplicador.Multiplicar(A, B)
imprimir.Imprimir(C)
