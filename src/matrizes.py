import sys
import os
import string

A = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

B = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

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







print("A triangular superior")

i = 0
j = 0
while(i < 4):
    if j < 4:
        print(f'{A[i][j]}\t', end = "")
        j = j + 1
    else:
        print("")
        i = i + 1
        j = i




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
