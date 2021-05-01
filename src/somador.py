def Somar(A, B):

    j = 0
    i = 0
    while(i < 4):
        if j < 4:
            A[i][j] = A[i][j] + B[i][j]
            j = j + 1
        else:
            i = i + 1
            j = 0

    return A
