import sys
import os
import string
import lerMatriz
import somador
import imprimir

A = lerMatriz.Ler("matriz_A.txt")
B = lerMatriz.Ler("matriz_B.txt")

print("A + B = C")
C = somador.Somar(A, B)
imprimir.Imprimir(C)
