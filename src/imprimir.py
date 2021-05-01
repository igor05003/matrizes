def Imprimir(A):
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
