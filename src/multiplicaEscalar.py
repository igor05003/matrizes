import sys
import os
import string
import lerMatriz
import escalar
import imprimir

A = lerMatriz.Ler("matriz_A.txt")


print("a*A = C")
a = float(input("a = " ))
C = escalar.Escalador(A, a)
imprimir.Imprimir(C)
